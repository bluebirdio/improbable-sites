from api.core.tables import *
from sqlalchemy import ForeignKey


class Team(TextIdentified, ImprobableDbModel, Description):
    pass


class TeamMember(ImprobableDbModel):
    team_id = Column(ForeignKey('team._id', ondelete='CASCADE'), nullable=False)
    role_id = Column(ForeignKey('role._id', ondelete='CASCADE'), nullable=False)
    user_id = Column(ForeignKey('user._id', ondelete='CASCADE'), nullable=False)
