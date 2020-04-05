from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import relationship

from samey.tables import *

from .values import RepositoryTargetType


class Repository(TextIdentified, SameyTable, HasDescription):
    url = Column(String(255))


class RepositoryTarget(SameyTable):
    repository_pk = Column(
        ForeignKey("repository.pk", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    target_type = Column(Enum(RepositoryTargetType))
    path = Column(String(255))

    repository = relationship("Repository", uselist=False)

    @property
    def repository_url(self):
        return self.repository.url
