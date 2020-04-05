from pydantic import EmailStr

from samey.models import *
from samey.table_crud import exists

from . import tables


class UserReference(BaseModel):
    user_id: str = ...

    @validator("user_id")
    def stack_exists(cls, value):
        if value is not None and not exists(tables.User, value):
            raise ValueError("invalid user_id")
        return value


class User(SameyTextIdentified, SameyModel):
    first_name: constr(min_length=1, max_length=30, strip_whitespace=True) = ...
    last_name: constr(min_length=1, max_length=30, strip_whitespace=True) = ...
    email: EmailStr = ...
