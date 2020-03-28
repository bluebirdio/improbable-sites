from api.core.tables import *
from sqlalchemy import ForeignKey


class App(TextIdentified, ImprobableDbModel, Description):
    team_id = Column(ForeignKey('team._id', ondelete='CASCADE'), nullable=False)
    production_url = Column(String(255))
    repository_url = Column(String(255))

