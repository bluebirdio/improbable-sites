from typing import List

from fastapi import APIRouter

from api.apps.tables import App
from api.core.db_crud import *
from api.instances import tables
from api.instances.models import *

router = APIRouter()


@router.get(
    "/{app_id}/instances",
    response_model=List[Instance],
    response_description="Return a list of apps_instances",
)
def list_app_instances(app_id: str):
    return query(tables.Instance, filter={"app_id": app_id})


@router.post(
    "/{app_id}/instances",
    status_code=201,
    response_model=Instance,
    response_description="Create a new instance.",
)
def create_app_instance(app_id: str, data_in: Instance):
    if exists_or_error(App, app_id):
        data_in.app_id = app_id
    if data_in.stack_id is None:
        # Get default instance_group for this app and set environment_id based on that.
        result = query(tables.InstanceGroup, app_id=app_id, default=True)
        if len(result) == 1:
            group = result[0]
            data_in.stack_id = group.stack_id
        # elseif there's no environment_id, throw error.
        # else create default instance group if there are none at all.

    return create(tables.Instance, data_in)


@router.get("/{app_id}/instances/{id}", response_model=Instance)
def get_app_instance(app_id: str, id: str):
    return get_or_error(
        tables.Instance,
        id,
        filter={"app_id": app_id},
        detail="Not an available instance.",
    )


@router.delete("/{apo_id}/instances/{id}", status_code=204)
def delete_app_instance(app_id: str, id: str):
    # Validate that the instance in this app namespace can be found
    if get_or_error(
        tables.Instance,
        id,
        filter={"app_id": app_id},
        detail="Not an available instance.",
    ):
        delete(tables.Instance, id)
