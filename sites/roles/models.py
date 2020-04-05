from samey.models import *
from samey.table_crud import exists

from . import tables


class RoleReference(BaseModel):
    role_id: str = ...

    @validator("role_id")
    def role_exists(cls, value):
        if value is not None and not exists(tables.Role, value):
            raise ValueError("invalid role_id")
        return value


class Role(HasDescription, SameyTextIdentified):
    pass
