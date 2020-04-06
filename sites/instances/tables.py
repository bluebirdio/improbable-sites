from sqlalchemy import Boolean, Enum, ForeignKey, UniqueConstraint

from samey.tables import *
from sites.repositories.values import RepositoryTargetType

from .values import ProductionLevel





class Instance(SameyTable):
    url = Column(String(255))
    application_id = Column(
        ForeignKey("application.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    stack_id = Column(
        ForeignKey("stack.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False
    )
    production_level = Column(Enum(ProductionLevel), nullable=False)
    instance_group_pk = Column(
        ForeignKey("application_instance_group.pk", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    repository_id = Column(
        ForeignKey("repository.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
    )
    repository_target_type = Column(Enum(RepositoryTargetType), nullable=True)
    repository_target = Column(String(255))

    __table_args__ = (
        UniqueConstraint("name", "application_id", name="unique_name_application_id"),
    )
