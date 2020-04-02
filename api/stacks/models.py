from api.core.db_crud import exists
from api.core.models import *

from . import tables


class Stack(HasDescription, ImprobableTextIdentified):
    parent_stack_id: str = None

    @validator("parent_stack_id")
    def parent_stack_exists(cls, value):
        if value is not None and not exists(tables.Stack, value):
            raise ValueError("parent_stack_id is invalie")
        return value
