from pydantic import AnyUrl

from samey.models import *

from .values import RepositoryTargetType


class Repository(HasDescription, ImprobableModel):
    url: AnyUrl = None


class RepositoryTarget(ImprobableModel):
    repository: Repository = ...
    target_type: RepositoryTargetType = ...
    path: AnyUrl = None
