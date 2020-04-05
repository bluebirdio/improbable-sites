from typing import List

from fastapi import APIRouter

from api.core.db_crud import *

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
    return create(tables.Application, app_in)


@router.get("/{id}", response_model=Application)
def get_application(id: str):
    return get_or_error(tables.Application, id, "App not found")


@router.put("/{id}", response_model=Application)
def update_application(*, id: str, app_in: Application):
    return update(tables.Application, id, app_in)


@router.delete("/{id}", status_code=204)
def delete_application(id: str):
    delete(tables.Application, id)
