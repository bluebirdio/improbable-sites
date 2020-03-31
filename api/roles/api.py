from fastapi import APIRouter

from .models import *
from . import tables

from api.core.db_crud import *
from typing import List

router = APIRouter()


@router.get(
    "/", response_model=List[Role], response_description="Return a list of roles"
)
def list_roles():
    return query(tables.Role)


@router.post("/", response_model=Role, response_description="Create a new role.")
def create_role(role_in: Role):
    return create(tables.Role, role_in)


@router.get("/{id}", response_model=Role)
def get_role(id: str):
    return get_or_error(tables.Role, id, "Role not found")


@router.delete("/{id}", response_model=Role)
def delete_role(id: str):
    return delete(tables.Role, id)
