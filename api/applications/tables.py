from sqlalchemy import ForeignKey

from api.core.tables import *


class Application(TextIdentified, ImprobableDbModel, Description):
    team_id = Column(
        ForeignKey("team.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
