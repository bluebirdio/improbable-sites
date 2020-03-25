from api.core.tables import *
from sqlalchemy import Text


class Stack(ImprobableDbModel, TextIdentified):
    description = Column(Text())

# Todo versions? major/minor? inheritance?
# Requirements e.g. database, php other environments.
# Related stacks e.g. solr...?
# Job specifications e.g. cron (these implementations would come from somewhere else ofc)

