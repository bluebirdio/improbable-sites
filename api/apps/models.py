from pydantic import AnyUrl

from api.core.models import *
from api.instances.models import Instance


class App(HasDescription, ImprobableTextIdentified):
    team_id: str = ...
    stack_id: str = ...
    production_url: Optional[AnyUrl] = None
    repository_url: Optional[AnyUrl] = None
