from samey.models import *


class Application(HasDescription, SameyTextIdentified):
    team_id: str = ...


#    production_url: Optional[AnyUrl] = None
#    repository_url: Optional[AnyUrl] = None
