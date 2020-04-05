from samey.table_crud import exists
from samey.models import *

from . import tables


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
