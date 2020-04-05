from pydantic import AnyUrl

from api.core.models import *

from .values import RepositoryTargetType


class Repository(HasDescription, ImprobableBaseModel):
    url: AnyUrl = None


class RepositoryTarget(ImprobableBaseModel):
    repository: Repository = ...
    target_type: RepositoryTargetType = ...
    path: AnyUrl = None
