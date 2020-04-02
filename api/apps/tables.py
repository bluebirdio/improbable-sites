from sqlalchemy import ForeignKey

from api.core.tables import *


class App(TextIdentified, ImprobableDbModel, Description):
    team_id = Column(ForeignKey("team._id", ondelete="CASCADE"), nullable=False)
    stack_id = Column(ForeignKey("stack._id", ondelete="RESTRICT"), nullable=False)
    production_url = Column(String(255), nullable=True)
    repository_url = Column(String(255), nullable=True)
