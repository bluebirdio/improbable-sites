from sqlalchemy import Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from samey.tables import *

from .values import Environment


class Instance(SameyTable):
    url = Column(String(255))

    application_id = Column(
        ForeignKey("application.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )

    stack_id = Column(
        ForeignKey("stack.id", onupdate="CASCADE", ondelete="RESTRICT"), nullable=False
    )

    environment = Column(Enum(Environment), nullable=False)

    instance_group = Column(String(255))

    __table_args__ = (
        UniqueConstraint("name", "application_id", name="unique_instance_name_application_id"),
    )
    application = relationship("Application", lazy="subquery")
