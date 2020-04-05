from samey.tables import *


class User(TextIdentified, ImprobableTable):
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(254), nullable=False)
