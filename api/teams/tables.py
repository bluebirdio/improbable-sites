from sqlalchemy import ForeignKey

from api.core.tables import *


class Team(TextIdentified, ImprobableTable, Description):
    pass


class TeamMember(ImprobableTable):
    team_id = Column(
        ForeignKey("team.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
    role_id = Column(
        ForeignKey("role.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False
    )
