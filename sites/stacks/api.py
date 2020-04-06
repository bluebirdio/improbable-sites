from typing import List

from fastapi import APIRouter

from samey.table_crud import *

from .models import *

router = APIRouter()


@router.get("/", response_model=List[Stack])
def list_stacks():
    return query(tables.Stack)


@router.post("/", response_model=Stack, status_code=201)
def create_stack(stack_in: Stack):
    return create(tables.Stack, stack_in)


@router.put("/{id}", response_model=Stack)
def update_stack(id: str, stack_in: Stack):
    return update(tables.Stack, id, stack_in)


@router.get("/{id}", response_model=Stack)
def get_stack(id: str):
    return get_or_error(tables.Stack, id, "Stack not found")


@router.delete("/{id}", status_code=204)
def delete_stack(id: str):
    delete(tables.Stack, id)
