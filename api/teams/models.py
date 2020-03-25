from api.core.models import *
from pydantic import SecretStr, Schema


class TeamMember(ImprobableBaseModel):
    team_id: SecretStr = ...
    role_id: SecretStr = ...
    user_id: SecretStr = ...


class Team(HasDescription, ImprobableTextIdentified):
    pass

