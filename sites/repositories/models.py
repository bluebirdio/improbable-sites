from pydantic import AnyUrl

from samey.models import *
from sites.teams.models import TeamReference

from .values import RepositoryTargetType


class RepositoryReference(BaseModel):
    repository_url: AnyUrl = None


class Repository(HasDescription, TeamReference, SameyModel):
    url: AnyUrl = None


class RepositoryTarget(SameyModel):
    repository: Repository = ...
    target_type: RepositoryTargetType = ...
    path: AnyUrl = None
