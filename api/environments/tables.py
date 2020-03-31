from sqlalchemy import Enum

from api.core.tables import *

from .values import ProductionLevel


class Environment(TextIdentified, ImprobableDbModel, Description):
    production_level = Column(Enum(ProductionLevel), nullable=False)
