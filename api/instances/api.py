from typing import List

from fastapi import APIRouter

from api.applications.tables import Application
from api.core.table_crud import *

from . import tables
from .models import *

# Top-level functions are included in the main app.
router = APIRouter()

# CRUD functions are namespaced under applications/{application_id}.
applications_router = APIRouter()


@router.get(
    "/",
    response_model=List[Instance],
    response_description="Return a list of all instances",
)
def list_app_instances():
    return query(tables.Instance)


@applications_router.get(
    "/",
    response_model=List[Instance],
    response_description="Return a list of apps_instances",
)
def list_app_instances(application_id: str):
    return query(tables.Instance, filter={"application_id": application_id})


@applications_router.post(
    "/",
    status_code=201,
    response_model=Instance,
    response_description="Create a new instance.",
)
def create_app_instance(application_id: str, data_in: Instance):
    if exists_or_error(Application, application_id):
        data_in.application_id = application_id
    if data_in.stack_id is None:
        # Get default instance_group for this app and set environment_id based on that.
        result = query(
            tables.InstanceGroup, application_id=application_id, default=True
        )
        if len(result) == 1:
            group = result[0]
            data_in.stack_id = group.stack_id
        # elseif there's no environment_id, throw error.
        # else create default instance group if there are none at all.

    return create(tables.Instance, data_in)


@applications_router.get("/{instance_id}", response_model=Instance)
def get_app_instance(application_id: str, instance_id: str):
    return get_or_error(
        tables.Instance,
        id,
        filter={"application_id": application_id},
        detail="Not an available instance.",
    )


@applications_router.delete("/{instance_id}", status_code=204)
def delete_app_instance(application_id: str, instance_id: str):
    # Validate that the instance in this app namespace can be found
    if get_or_error(
        tables.Instance,
        id,
        filter={"application_id": application_id},
        detail="Not an available instance.",
    ):
        delete(tables.Instance, id)
