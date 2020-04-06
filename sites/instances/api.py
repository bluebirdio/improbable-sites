from typing import List

from fastapi import APIRouter

from samey.table_crud import *
from sites.applications.tables import Application

from .models import *

# Top-level functions are included in the main app.
router = APIRouter()


@router.get("/",response_model=List[Instance])
def list_instances():
    return query(tables.Instance)


@router.post("/",status_code=201,response_model=Instance)
def create_instance(data_in: Instance):
    return create(tables.Instance, data_in)


@router.put("/{id}", response_model=Instance)
def update_instance(id: str, data_in: Instance):
    return update(tables.Instance, id, data_in)


@router.delete("/{id}", status_code=204)
def delete_instance(id: str):
    delete(tables.Instance, id)


# Instances belong to applications and applications/apy.py will include these functions under applications/{id}.
applications_router = APIRouter()


@applications_router.get("/", response_model=List[Instance])
def list_application_instances(application_id: str):
    return query(tables.Instance, application_id=application_id)


@applications_router.get("/{name}", response_model=Instance)
def get_application_instance(application_id: str, name: str):
    return get_instance(application_id, name)


@applications_router.delete("/{name}", status_code=204)
def delete_application_instance(application_id: str, name: str):
    instance = get_instance(application_id, name)
    delete(tables.Instance, instance.id)


def get_instance(application_id: str, name: str):
    """
    Helper function to load an instance under its application scope.
    :param application_id: String identifier for application
    :param name: Instance name, unique to this application.
    :return: Instance
    """
    return get_or_error(
        tables.Instance,
        application_id=application_id,
        name=name,
        detail="Not an available instance.",
    )
