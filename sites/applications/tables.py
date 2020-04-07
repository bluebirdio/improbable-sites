from sqlalchemy import Boolean, ForeignKey, SmallInteger, UniqueConstraint
from sqlalchemy.orm import relationship

from samey.tables import *


class Application(TextIdentified, SameyTable, HasDescription):
    team_id = Column(
        ForeignKey("team.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )

    repository_url = Column(String(255), nullable=True)

    instance_groups = relationship("ApplicationInstanceGroup", lazy="subquery")


class ApplicationInstanceGroup(SameyTable):
    application_id = Column(
        ForeignKey("application.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    sort = Column(SmallInteger)

    stack_id = Column(
        ForeignKey("stack.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=True
    )
    repository_url = Column(String(255), nullable=True)

    __table_args__ = (
        UniqueConstraint("name", "application_id", name="unique_application_instance_group_name_application_id"),
    )
