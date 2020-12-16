from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression, func

from ..Base import Base


class Project(Base):
    __tablename__ = "Project"

    id = Column(Text, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False)

    name = Column(Text, nullable=False)

    workspace_id = Column(
        Text,
        ForeignKey("Workspace.id", ondelete="CASCADE"),
        nullable=False,
    )
