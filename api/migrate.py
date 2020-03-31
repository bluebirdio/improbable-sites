import sqlalchemy
from api.settings import DATABASE_URL
from api.users.tables import *
from api.roles.tables import *
from api.teams.tables import *
from api.environments.tables import *
from api.apps.tables import *
from api.instances.tables import *
from api.repositories.tables import *


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


def main():
    ImprobableDbModel.metadata.create_all(engine)


main()
