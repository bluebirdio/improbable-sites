from pydantic import EmailStr

from api.core.models import *


class User(ImprobableTextIdentified, ImprobableBaseModel):
    first_name: constr(min_length=1, max_length=30, strip_whitespace=True) = ...
    last_name: constr(min_length=1, max_length=30, strip_whitespace=True) = ...
    email: EmailStr = ...
