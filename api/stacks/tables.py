from sqlalchemy import ForeignKey

from api.core.tables import *


class Stack(TextIdentified, ImprobableDbModel, Description):
    parent_stack_id = Column(
        ForeignKey("stack._id", ondelete="RESTRICT"), nullable=True
    )


# Todo versions? major/minor? inheritance?
# Requirements e.g. database, php other environments.
# Related stacks e.g. solr...?
# Job specifications e.g. cron (these implementations would come from somewhere else ofc)
