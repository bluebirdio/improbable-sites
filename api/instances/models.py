from api.core.models import *
from pydantic import AnyUrl


class Instance(ImprobableBaseModel):
    app_id: str = ...
    environment_id: str = ...
    url: Optional[AnyUrl] = None
