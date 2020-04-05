from sqlalchemy import ForeignKey

from samey.tables import *


class Application(TextIdentified, ImprobableTable, Description):
    team_id = Column(
        ForeignKey("team.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
