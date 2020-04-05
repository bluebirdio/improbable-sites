from pydantic import AnyUrl

from api.core.models import *


class Application(HasDescription, ImprobableTextIdentified):
    team_id: str = ...


#    production_url: Optional[AnyUrl] = None
#    repository_url: Optional[AnyUrl] = None
