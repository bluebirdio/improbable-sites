from api.core.models import *
from .values import ProductionLevel


class Environment(HasDescription, ImprobableTextIdentified, ImprobableBaseModel):
    production_level: ProductionLevel = ...
