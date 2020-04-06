from pydantic import AnyUrl

from samey.models import *
from samey.table_crud import exists
from sites.applications.models import (
    ApplicationInstanceGroupReference,
    ApplicationReference,
)
from sites.repositories.values import RepositoryTargetType
from sites.stacks.models import StackReference

from . import tables
from .values import ProductionLevel


class Instance(
    StackReference, ApplicationInstanceGroupReference, ApplicationReference, SameyModel
):
    production_level: ProductionLevel = ...
    url: Optional[AnyUrl] = None
    # repository_url: str = ...
    # repository_target_type: RepositoryTargetType = ...
    # repository_target: str = ...
