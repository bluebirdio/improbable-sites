from pydantic import SecretStr

from samey.models import *
from samey.table_crud import exists
from sites.roles.models import RoleReference
from sites.users.models import UserReference

from . import tables


class TeamReference(BaseModel):
    team_id: str = ...

    @validator("team_id")
    def stack_exists(cls, value):
        if value is not None and not exists(tables.Team, value):
            raise ValueError("invalid team_id")
        return value


class TeamMember(UserReference, RoleReference, TeamReference, SameyModel):
    pass


class Team(HasDescription, SameyTextIdentified):
    pass
