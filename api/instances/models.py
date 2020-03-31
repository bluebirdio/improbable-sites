from pydantic import AnyUrl

from api.core.models import *


class Instance(ImprobableBaseModel):
    app_id: str = ...
    environment_id: str = ...
    url: Optional[AnyUrl] = None
