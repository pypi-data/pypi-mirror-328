import random
from string import Template

from .app_base import *
from fastapi import Depends
from fastapi.routing import APIRouter
from contextlib import suppress

from ..eng.errors import *
from ..eng.user import UserRecord, UserDatabase, validate_username
from ..eng.docker import ContainerAction, ContainerConfig, \
    create_container, container_action, list_docker_containers, get_docker_used_ports, inspect_container, exec_container_bash, check_container

from ..config import config

router_pod = APIRouter(prefix="/pod")

def eval_ins_name(ins: str, user: UserRecord):
    if '-' in ins:
        ins_sp = ins.split('-')
        if not ins_sp[0] == user.name and not user.is_admin:
            raise InsufficientPermissionsError("Invalid pod name")
        return ins
    return f"{user.name}-{ins}"

@router_pod.post("/create")
@handle_exception
def create_pod(ins: str, image: str, user: UserRecord = Depends(require_permission("all"))):
    validate_username(ins)
    server_config = config()
    container_name = f"{user.name}-{ins}"

    # first check if the container exists
    with suppress(ContainerNotFoundError):
        check_container(g_client, container_name)
        raise DuplicateError(f"Container {container_name} already exists")

    # check user quota
    user_quota = UserDatabase().check_user_quota(user.name)
    user_containers = list_docker_containers(g_client, user.name + '-')
    if user_quota.max_pods != -1 and user_quota.max_pods <= len(user_containers):
        raise PermissionError("Exceed max pod limit")

    # check image
    allowed_images = [i_image.name for i_image in server_config.images]
    if image not in allowed_images:
        raise PermissionError(f"Image {image} is not allowed")

    # hanlding port
    def to_individual_port(ports: list[int | tuple[int, int]]) -> list[int]:
        res = []
        for port in ports:
            if isinstance(port, tuple):
                res.extend(range(port[0], port[1]+1))
            else:
                res.append(port)
        return res

    used_port_list = get_docker_used_ports(g_client)
    available_port_list = list(set(to_individual_port(server_config.available_ports)) - set(used_port_list))

    target_image = [i_image for i_image in server_config.images if i_image.name == image][0]
    target_ports = target_image.ports
    if len(target_ports) > len(available_port_list):
        raise PermissionError("No available port")
    
    random.shuffle(available_port_list)
    port_mapping = [f'{available_port_list[i]}:{target_ports[i]}' for i in range(len(target_ports))]

    # handling volume
    volume_mappings = [Template(mapping).substitute(username=user.name) for mapping in server_config.volume_mappings]

    # create container
    container_config = ContainerConfig(
        image_name=image,
        container_name=container_name,
        volumes=volume_mappings,
        port_mapping=port_mapping,
        gpu_ids=None,
        memory_limit=f'{user_quota.memory_limit}b' if user_quota.memory_limit > 0 else None,
        storage_limit=f'{user_quota.storage_limit}b' if user_quota.storage_limit > 0 else None, 
    )
    log = create_container(g_client, container_config) 
    try: container_info = inspect_container(g_client, container_name)
    except Exception as e: container_info = None
    return {"log": log, "info": container_info}

@router_pod.post("/delete")
@handle_exception
def delete_pod(ins: str, user: UserRecord = Depends(require_permission("all"))):
    container_name = eval_ins_name(ins, user)
    return {"log": container_action(g_client, container_name, ContainerAction.DELETE)}

@router_pod.post("/restart")
@handle_exception
def restart_pod(ins: str, user: UserRecord = Depends(require_permission("all"))):
    container_name = eval_ins_name(ins, user)
    return {"log": container_action(g_client, container_name, ContainerAction.RESTART, after_action="service ssh restart")}

@router_pod.post("/stop")
@handle_exception
def stop_pod(ins: str, user: UserRecord = Depends(require_permission("all"))):
    container_name = eval_ins_name(ins, user)
    return {"log": container_action(g_client, container_name, ContainerAction.STOP)}

@router_pod.post("/start")
@handle_exception
def start_pod(ins: str, user: UserRecord = Depends(require_permission("all"))):
    container_name = eval_ins_name(ins, user)
    return {"log": container_action(g_client, container_name, ContainerAction.START, after_action="service ssh restart")}

@router_pod.get("/info")
@handle_exception
def info_pod(ins: str, user: UserRecord = Depends(require_permission("all"))):
    container_name = eval_ins_name(ins, user)
    return inspect_container(g_client, container_name)

@router_pod.get("/list")
@handle_exception
def list_pod(user: UserRecord = Depends(require_permission("all"))):
    return list_docker_containers(g_client, user.name + '-')

@router_pod.post("/exec")
@handle_exception
def exec_pod(ins: str, cmd: str, user: UserRecord = Depends(require_permission("all"))):
    container_name = eval_ins_name(ins, user)
    exit_code, log = exec_container_bash(container_name, cmd)
    return {"exit_code": exit_code, "log": log}

# ====== admin only ======
@router_pod.get("/listall")
@handle_exception
def listall_pod(user: UserRecord = Depends(require_permission("admin"))):
    return list_docker_containers(g_client, "")
