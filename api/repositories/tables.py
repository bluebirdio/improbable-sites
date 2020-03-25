from api.core.tables import *


class Repository(ImprobableDbModel, TextIdentified, Description):
    url = Column(String(255))
