from pydantic import AnyUrl

from api.core.models import *


class Repository(HasDescription, ImprobableBaseModel):
    url: AnyUrl = None
