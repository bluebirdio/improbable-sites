from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, Field, constr, root_validator, validator
from slugify import slugify


class ImprobableModel(BaseModel):
    id: Optional[str] = Field(
        None, title="Automatically-generated unique identifier", readOnly=True
    )
    name: constr(min_length=2, max_length=255, strip_whitespace=True) = ...

    class Config:
        orm_mode = True


class ImprobableTextIdentified(ImprobableModel):
    id: constr(min_length=2, max_length=255, strip_whitespace=True) = None

    @root_validator
    def set_id(cls, values):
        if values["id"] is None:
            if "name" in values:
                values["id"] = slugify(values["name"])
            else:
                ValueError("Must specify id or name")
        return values


class ImprobableInternalAttributes(BaseModel):
    uuid: UUID4
    created: datetime = datetime.utcnow()
    changed: datetime = None


class HasDescription(BaseModel):
    description: Optional[str] = None
