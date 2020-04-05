from typing import List

from fastapi import APIRouter

from api.core.db_crud import *

from . import tables
from .models import *

router = APIRouter()


@router.get(
    "/",
    response_model=List[Instance],
    response_description="Return a list of all instances",
)
def list_app_instances():
    return query(tables.Instance)


# CRUD functions are in apps_instances and namespaced under app/{app_id}.
