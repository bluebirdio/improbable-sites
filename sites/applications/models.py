from typing import List

from samey.models import *
from samey.table_crud import exists
from sites.teams.models import TeamReference

from . import tables


class ApplicationInstanceGroupReference(BaseModel):
    instance_group: str = Field(default="default")

    @validator("instance_group", pre=True)
    def instance_group_exists(cls, value, values):
        if "application_id" not in values:
            raise ValueError("unable to validate instance_group without a valid application_id")

        application_id = values["application_id"]
        if not exists(
            tables.ApplicationInstanceGroup, name=value, application_id=application_id
        ):
            raise ValueError("invalid instance_group")
        return value


class ApplicationReference(BaseModel):
    application_id: str = Field(..., example="example.com")

    @validator("application_id")
    def application_exists(cls, value):
        if value is not None and not exists(tables.Application, value):
            raise ValueError("invalid application_id")
        return value


class ApplicationInstanceGroup(ApplicationReference, SameyModel):
    name: constr(
        min_length=2, max_length=32, strip_whitespace=True, regex="[a-zA-Z0-9-.]"
    ) = Field(..., example="backend")


class Application(HasDescription, TeamReference, SameyTextIdentified):
    instance_groups: List[ApplicationInstanceGroup] = Field([], readOnly=True)


#    production_url: Optional[AnyUrl] = None
#    repository_url: Optional[AnyUrl] = None
