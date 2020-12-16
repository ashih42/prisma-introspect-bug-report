from sqlalchemy import *
from sqlalchemy.sql import expression, func

from ..Base import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Text, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False)

    email = Column(Text, nullable=False, unique=True)
