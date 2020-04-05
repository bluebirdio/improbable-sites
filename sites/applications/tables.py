from sqlalchemy import ForeignKey

from samey.tables import *


class Application(TextIdentified, SameyTable, HasDescription):
    team_id = Column(
        ForeignKey("team.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
