from pydantic import AnyUrl

from samey.models import *

from .values import RepositoryTargetType


class Repository(HasDescription, SameyModel):
    url: AnyUrl = None


class RepositoryTarget(SameyModel):
    repository: Repository = ...
    target_type: RepositoryTargetType = ...
    path: AnyUrl = None
