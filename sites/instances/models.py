from pydantic import AnyUrl

from samey.models import *
from samey.table_crud import exists
from sites.applications.models import ApplicationReference
from sites.repositories.values import RepositoryTargetType
from sites.stacks.models import StackReference

from . import tables
from .values import ProductionLevel


class InstanceGroupReference(BaseModel):
    instance_group_id: str = ...

    @validator("instance_group_id")
    def instance_group_exists(cls, value):
        if value is not None and not exists(tables.InstanceGroup, value):  # TODO APP_ID
            raise ValueError("invalid instance_group")
        return value


class Instance(
    StackReference, InstanceGroupReference, ApplicationReference, SameyModel
):
    production_level: ProductionLevel = ...
    url: Optional[AnyUrl] = None
    repository_url: str = ...
    repository_target_type: RepositoryTargetType = ...
    repository_target: str = ...
