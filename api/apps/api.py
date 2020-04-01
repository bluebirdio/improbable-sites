from typing import List

from fastapi import APIRouter

from api.core.db_crud import *

from . import tables
from .models import *

router = APIRouter()


@router.get(
    "/", response_model=List[App], response_description="Return a list of applications"
)
def list_apps():
    return query(tables.App)


@router.post("/", response_model=App, status_code=201, response_description="Create a new app.")
def create_app(app_in: App):
    return create(tables.App, app_in)


@router.get("/{id}", response_model=App)
def get_app(id: str):
    return get_or_error(tables.App, id, "App not found")


@router.put("/{id}", response_model=App)
def update_app(*, id: str, app_in: App):
    return update(tables.App, id, app_in)


@router.delete("/{id}", status_code=204)
def delete_app(id: str):
    delete(tables.App, id)


@router.get("/{id}/{environment}", response_model=Instance)
def get_app_instance(id: str):
    app = get_or_error(tables.App, id)
    return app


@router.put("/{id}/{environment}", response_model=Instance)
def update_app_instance(*, id: str, app_in: App):
    app = get_or_error(tables.App, id)

    app_data = db_process_input(app_in, app)
    if app_data:
        return update(tables.App, app=app, data=app_data)
    else:
        return app


@router.delete("/{id}/{environment}", status_code=204)
def delete_app(id: str):
    app = get_or_error(tables.App, id)
    delete(app)
