import re
from datetime import datetime
from uuid import uuid4

import shortuuid
from slugify import slugify
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_utils.types.uuid import UUIDType


class ImprobableBaseDbModel:
    @declared_attr
    def __tablename__(self):
        # Generate __tablename__ automatically by turning CamelCase class name to snake_case
        snake = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", self.__name__)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", snake).lower()

    @declared_attr
    def __table_args__(self):
        return {"mysql_engine": "InnoDB"}

    pk = Column(Integer(), primary_key=True)
    # uuid = Column(UUID(as_uuid=True), default=uuid4, nullable=False, index=True, unique=True)
    # TODO uuid column is pgsql-specific revert w/ pgsql or find a longer-term solution.
    uuid = Column(UUIDType(), nullable=False, default=uuid4)
    name = Column(String(255), nullable=False)
    created = Column(DateTime(), default=datetime.utcnow)
    changed = Column(DateTime())

    @hybrid_property
    def id(self):
        try:
            return shortuuid.encode(self.uuid)
        except AttributeError:
            return

    @id.setter
    def id(self, set_id):
        if set_id is str:
            uuid = shortuuid.decode(set_id)
            if uuid is UUID4:
                self.uuid = shortuuid.decode(set_id)

    def __str__(self):
        return self.name


ImprobableDbModel = declarative_base(cls=ImprobableBaseDbModel)


class TextIdentified:
    _id = Column(String(255), nullable=False, index=True, unique=True)

    @hybrid_property
    def id(self):
        if self._id is None:
            self._id = slugify(self.name)
        return self._id

    @id.setter
    def id(self, set_id):
        if set_id is not None:
            self._id = slugify(set_id)
        elif self.name is not None:
            self._id = slugify(self.name)


class Description(object):
    description = Column(Text())
