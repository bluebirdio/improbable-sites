from sqlalchemy import ForeignKey

from api.core.tables import *


class Application(TextIdentified, ImprobableDbModel, Description):
    team_id = Column(
        ForeignKey("team._id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
