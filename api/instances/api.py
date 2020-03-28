from fastapi import APIRouter

from .models import *
from . import tables

from api.core.db_crud import *
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Instance], response_description="Return a list of all instances")
def list_app_instances():
    return query(tables.Instance)

# CRUD functions are in apps_instances and namespaced under the app/{app_id} space.
