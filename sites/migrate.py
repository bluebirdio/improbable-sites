import sqlalchemy

from sites.applications.tables import *
from sites.instances.tables import *
from sites.repositories.tables import *
from sites.roles.tables import *
from sites.settings import DATABASE_URL
from sites.stacks.tables import *
from sites.teams.tables import *
from sites.users.tables import *

engine = sqlalchemy.create_engine(DATABASE_URL)


def create_all():
    SameyTable.metadata.create_all(engine)


def drop_all():
    SameyTable.metadata.drop_all(engine)


create_all()
