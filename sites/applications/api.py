from typing import List

from fastapi import APIRouter

from samey.table_crud import *
from sites.instances.api import applications_router

from . import tables
from .models import *

router = APIRouter()


@router.get(
    "/",
    response_model=List[Application],
    response_description="Return a list of applications",
)
def list_applications():
    return query(tables.Application)


@router.post(
    "/",
    response_model=Application,
    status_code=201,
    response_description="Create a new app.",
)
def create_application(app_in: Application):
    application = create(tables.Application, app_in)

    # Create a default instance group.
    default_instance_group = ApplicationInstanceGroup(application_id=application.id, name="default", default=True)
    create(tables.ApplicationInstanceGroup, default_instance_group)

    # Return a reloaded application that includes the instance.
    return get_or_error(tables.Application, application.id)


@router.get("/{id}", response_model=Application)
def get_application(id: str):
    return get_or_error(tables.Application, id, "App not found")


@router.put("/{id}", response_model=Application)
def update_application(*, id: str, app_in: Application):
    return update(tables.Application, id, app_in)


@router.delete("/{id}", status_code=204)
def delete_application(id: str):
    delete(tables.Application, id)


router.include_router(applications_router, prefix="/{id}/instances")
