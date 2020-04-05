import sqlalchemy

from api.apps.tables import *
from api.instances.tables import *
from api.repositories.tables import *
from api.roles.tables import *
from api.settings import DATABASE_URL
from api.stacks.tables import *
from api.teams.tables import *
from api.users.tables import *

engine = sqlalchemy.create_engine(DATABASE_URL)


def create_all():
    ImprobableDbModel.metadata.create_all(engine)


def drop_all():
    ImprobableDbModel.metadata.drop_all(engine)


create_all()
