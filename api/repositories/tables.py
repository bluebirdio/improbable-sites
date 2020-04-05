from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import relationship

from api.core.tables import *

from .values import RepositoryTargetType


class Repository(TextIdentified, ImprobableDbModel, Description):
    url = Column(String(255))


class RepositoryTarget(ImprobableDbModel):
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
