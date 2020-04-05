from pydantic import AnyUrl

from api.core.db_crud import exists
from api.core.models import *
from api.environments import tables as env_tables
from api.repositories.values import RepositoryTargetType
from api.stacks import tables as stack_tables

from . import tables


class Instance(ImprobableBaseModel):
    app_id: str = ...
    instance_group_id: str = ...
    environment_id: str = ...
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

    @validator("environment_id")
    def environment_exists(cls, value):
        if not exists(env_tables.Environment, value):
            raise ValueError("invalid environment_id")
        return value

    @validator("stack_id")
    def stack_exists(cls, value):
        if value is not None and not exists(stack_tables.Stack, value):
            raise ValueError("invalid stack_id")
        return value
