from pydantic import AnyUrl

from samey.table_crud import exists
from samey.models import *
from api.repositories.values import RepositoryTargetType
from api.stacks import tables as stack_tables

from . import tables
from .values import ProductionLevel


class Instance(SameyModel):
    app_id: str = ...
    instance_group_id: str = ...
    production_level: ProductionLevel = ...
    stack_id: str = ...
    url: Optional[AnyUrl] = None
    repository_url: str = ...
    repository_target_type: RepositoryTargetType = ...
    repository_target: str = ...

    @validator("instance_group_id")
    def instance_group_exists(cls, value):
        if value is not None and not exists(tables.InstanceGroup, value):  # TODO APP_ID
            raise ValueError("invalid instance_group")
        return value

    @validator("stack_id")
    def stack_exists(cls, value):
        if value is not None and not exists(stack_tables.Stack, value):
            raise ValueError("invalid stack_id")
        return value
