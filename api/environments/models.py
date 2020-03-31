from api.core.models import *

from .values import ProductionLevel


class Environment(HasDescription, ImprobableTextIdentified):
    production_level: ProductionLevel = ...
