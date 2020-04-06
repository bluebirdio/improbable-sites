from typing import List

from fastapi import APIRouter

from samey.table_crud import *

from . import tables
from .models import *

router = APIRouter()


@router.get("/", response_model=List[Role])
def list_roles():
    return query(tables.Role)


@router.post("/", response_model=Role, status_code=201)
def create_role(role_in: Role):
    return create(tables.Role, role_in)


@router.get("/{id}", response_model=Role)
def get_role(id: str):
    return get_or_error(tables.Role, id, "Role not found")


@router.delete("/{id}", status_code=204)
def delete_role(id: str):
    delete(tables.Role, id)
