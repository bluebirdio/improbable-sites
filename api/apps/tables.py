from api.core.tables import *
from sqlalchemy import ForeignKey


class App(TextIdentified, ImprobableDbModel, Description):
    team_id = Column(ForeignKey('team._id', ondelete='CASCADE'), nullable=False)
    production_url = Column(String(255))
    repository_url = Column(String(255))


class AppInstance(ImprobableDbModel):
    url = Column(String(255))
    app_id = Column(ForeignKey('app._id', ondelete='CASCADE'), nullable=False)
    environment_id = Column(ForeignKey('environment._id', ondelete='RESTRICT'), nullable=False)
