from pydantic import BaseModel, constr, UUID4, Field, validator
from typing import Optional
from datetime import datetime
import slugify


class ImprobableBaseModel(BaseModel):
    id: Optional[str] = Field(
        None, title="Automatically-generated unique identifier", readOnly=True
    )
    name: constr(min_length=2, max_length=255, strip_whitespace=True) = ...

    class Config:
        orm_mode = True


class ImprobableTextIdentified(ImprobableBaseModel):
    id: constr(min_length=2, max_length=255, strip_whitespace=True) = None

    @validator("id", always=True)
    def set_id(cls, v, values):
        if v is not None:
            return v
        elif "name" in values:
            return v or slugify(values["name"])


class ImprobableInternalAttributes(BaseModel):
    uuid: UUID4
    created: datetime = datetime.utcnow()
    changed: datetime = None


class HasDescription(BaseModel):
    description: Optional[str] = None
