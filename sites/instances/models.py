from pydantic import AnyUrl

from samey.models import *
from samey.table_crud import db_get
from sites.applications.models import (
    Application,
    ApplicationInstanceGroupReference,
    ApplicationReference,
)
from sites.stacks.models import StackReference

from . import tables
from .values import Environment


class Instance(
    StackReference, ApplicationInstanceGroupReference, ApplicationReference, SameyModel
):
    application: Application = Field(None, readOnly=True)
    environment: Environment = ...
    url: Optional[AnyUrl] = None
    # repository_target_type: RepositoryTargetType = ...
    # repository_target: str = ...

    @root_validator()
    def unique_name(cls, values):
        if (
            "application_id" in values
            and "name" in values
            and "instance_group" in values
        ):
            item = db_get(
                tables.Instance,
                application_id=values["application_id"],
                instance_group=values["instance_group"],
                name=values["name"],
            )
            if item is not None:
                if "id" not in values or item.id != values["id"]:
                    raise ValueError("Name is not unique.",)
        return values
