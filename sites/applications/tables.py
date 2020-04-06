from sqlalchemy import Boolean, ForeignKey, SmallInteger, UniqueConstraint
from sqlalchemy.orm import relationship

from samey.tables import *


class Application(TextIdentified, SameyTable, HasDescription):
    team_id = Column(
        ForeignKey("team.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
    instance_groups = relationship("ApplicationInstanceGroup", lazy="subquery")


class ApplicationInstanceGroup(SameyTable):
    application_id = Column(
        ForeignKey("application.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    sort = Column(SmallInteger)

    # TODO do these live here or can they be derived from the prod URL?
    stack_id = Column(
        ForeignKey("stack.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=True
    )
    repository_id = Column(
        ForeignKey("repository.id", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=True,
    )

    __table_args__ = (
        UniqueConstraint("name", "application_id", name="unique_name_application_id"),
    )
