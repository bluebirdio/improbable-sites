from samey.models import *
from samey.table_crud import exists
from sites.teams.models import TeamReference

from . import tables


class ApplicationReference(BaseModel):
    application_id: str = ...

    @validator("application_id")
    def application_exists(cls, value):
        if value is not None and not exists(tables.Application, value):
            raise ValueError("invalid application_id")
        return value


class Application(HasDescription, TeamReference, SameyTextIdentified):
    pass


#    production_url: Optional[AnyUrl] = None
#    repository_url: Optional[AnyUrl] = None
