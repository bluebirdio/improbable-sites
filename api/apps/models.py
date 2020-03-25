from api.core.models import *
from pydantic import AnyUrl


class AppInstance(ImprobableBaseModel):
    app_id: str = ...
    environment_id: str = ...
    url: Optional[AnyUrl] = None


class App(HasDescription, ImprobableTextIdentified):
    team_id: str = ...
    production_url: Optional[AnyUrl] = None
    repository_url: Optional[AnyUrl] = None
