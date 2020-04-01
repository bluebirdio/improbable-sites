from typing import List

from fastapi import APIRouter

from api.core.db_crud import *

from . import tables
from .models import *

router = APIRouter()


@router.get(
    "/",
    response_model=List[Environment],
    response_description="Return a list of environments",
)
def list_environments():
    return query(tables.Environment)


@router.post(
    "/", response_model=Environment, status_code=201, response_description="Create a new environment."
)
def create_environment(env_in: Environment):
    return create(tables.Environment, env_in)


@router.get("/{id}", response_model=Environment)
def get_environment(id: str):
    return get_or_error(tables.Environment, id, "Not an available environment.")


@router.delete("/{id}", status_code=204)
def delete_environment(id: str):
    delete(tables.Environment, id)
