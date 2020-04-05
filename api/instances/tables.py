from sqlalchemy import Boolean, Enum, ForeignKey, UniqueConstraint

from api.core.tables import *
from api.repositories.values import RepositoryTargetType

from .values import ProductionLevel


class InstanceGroup(ImprobableDbModel):
    default = Column(Boolean, default=False)
    application_id = Column(
        ForeignKey("application._id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    stack_id = Column(
        ForeignKey("stack._id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False
    )
    repository_id = Column(
        ForeignKey("repository._id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )

    __table_args__ = (UniqueConstraint("name", "application_id", name="unique_name_application_id"),)


class Instance(ImprobableDbModel):
    url = Column(String(255))
    application_id = Column(
        ForeignKey("application._id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    stack_id = Column(
        ForeignKey("stack._id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False
    )
    production_level = Column(Enum(ProductionLevel), nullable=False)
    instance_group_pk = Column(
        ForeignKey("instance_group.pk", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    repository_id = Column(
        ForeignKey("repository._id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    repository_target_type = Column(Enum(RepositoryTargetType), nullable=True)
    repository_target = Column(String(255))
