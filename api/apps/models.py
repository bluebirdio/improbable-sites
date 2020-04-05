from pydantic import AnyUrl

from api.core.models import *


class App(HasDescription, ImprobableTextIdentified):
    team_id: str = ...


#    production_url: Optional[AnyUrl] = None
#    repository_url: Optional[AnyUrl] = None
