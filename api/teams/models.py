from pydantic import SecretStr

from samey.models import *


class TeamMember(ImprobableModel):
    team_id: SecretStr = ...
    role_id: SecretStr = ...
    user_id: SecretStr = ...


class Team(HasDescription, ImprobableTextIdentified):
    pass
