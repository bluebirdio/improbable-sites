from typing import List

from fastapi import APIRouter

from api.core.table_crud import *

from . import tables
from .models import *

router = APIRouter()


@router.get(
    "/", response_model=List[User], response_description="Return a list of users"
)
def list_users():
    return query(tables.User)


@router.post(
    "/", response_model=User, status_code=201, response_description="Create a new user."
)
def create_user(user_in: User):
    return create(tables.User, user_in)


@router.get("/{id}", response_model=User)
def get_user(id: str):
    return get_or_error(tables.User, id, "User not found")


@router.delete("/{id}", status_code=204)
def delete_user(id: str):
    delete(tables.User, id)
