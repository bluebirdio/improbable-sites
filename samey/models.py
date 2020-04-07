from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, Field, constr, root_validator, validator
from slugify import slugify


class SameyModel(BaseModel):
    id: Optional[str] = Field(
        None,
        title="Automatically-generated unique identifier",
        readOnly=True,
        example="U45VpinDPVetdEjNMF7sdo",
    )
    name: constr(min_length=2, max_length=255, strip_whitespace=True) = Field(
        ..., example="My stuff"
    )

    class Config:
        orm_mode = True


class SameyTextIdentified(SameyModel):
    id: constr(min_length=2, max_length=255, strip_whitespace=True) = Field(
        None, example="item-id"
    )

    @root_validator
    def set_id(cls, values):
        if values["id"] is None:
            if "name" in values:
                values["id"] = slugify(values["name"])
            else:
                ValueError("Must specify id or name")
        return values


class SameyProperties(BaseModel):
    uuid: UUID4
    created: datetime = datetime.utcnow()
    changed: datetime = None


class HasDescription(BaseModel):
    description: Optional[str] = Field(None, example="User-supplied description.")
