from samey.models import *
from samey.table_crud import exists

from . import tables


class StackReference(BaseModel):
    stack_id: str = ...

    @validator("stack_id")
    def stack_exists(cls, value):
        if value is not None and not exists(tables.Stack, value):
            raise ValueError("invalid stack_id")
        return value


class Stack(HasDescription, SameyTextIdentified):
    id: constr(
        min_length=2, max_length=15, strip_whitespace=True, regex="[a-z0-9]"
    ) = None
    parent_stack_id: str = None

    @validator("parent_stack_id")
    def parent_stack_exists(cls, value):
        if value is not None and not exists(tables.Stack, value):
            raise ValueError("parent_stack_id is invalid")
        return value
