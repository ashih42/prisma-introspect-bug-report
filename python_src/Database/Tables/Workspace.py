from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression, func

from ..Base import Base


class Workspace(Base):
    __tablename__ = "Workspace"

    id = Column(Text, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False)

    name = Column(Text, nullable=False)
