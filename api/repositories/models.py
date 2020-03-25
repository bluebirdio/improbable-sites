from api.core.models import *
from pydantic import AnyUrl


class Repository(HasDescription, ImprobableBaseModel):
    url: AnyUrl = None
