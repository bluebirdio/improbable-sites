from fastapi import APIRouter

from api.instances import tables
from api.instances.models import *

from api.core.db_crud import *
from typing import List

router = APIRouter()


@router.get("/{app_id}/instances", response_model=List[Instance], response_description="Return a list of apps_instances")
def list_app_instances(app_id: str):
    return query(tables.Instance, filter={'app_id': app_id})


@router.post("/{app_id}/instances", response_model=Instance, response_description="Create a new instance.")
def create_app_instance(app_id: str, data_in: Instance):
    app = get_or_error(tables.App, app_id, "Invalid app id.")
    data_in.app_id = app.app_id
    return create(tables.Instance, data_in)


@router.get("/{app_id}/instances/{id}", response_model=Instance)
def get_app_instance(app_id: str, id: str):
    return get_or_error(tables.Instance, id, filter={'app_id': app_id}, detail="Not an available instance.")


@router.delete("/{app_id}/instances/{id}", response_model=Instance)
def delete_app_instance(app_id: str, id: str):
    # Validate that the instance in this app namespace can be found
    if get_or_error(tables.Instance, id, filter={'app_id': app_id}, detail="Not an available instance."):
        return delete(tables.Instance, id)

