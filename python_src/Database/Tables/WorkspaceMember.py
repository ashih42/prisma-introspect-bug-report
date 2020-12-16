from sqlalchemy import *
from sqlalchemy.dialects.postgresql import JSONB, ENUM
from sqlalchemy.sql import expression, func
from sqlalchemy.schema import UniqueConstraint

from ..Base import Base


class WorkspaceMember(Base):
    __tablename__ = "WorkspaceMember"

    id = Column(Text, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False)

    role = Column(Text, nullable=False)

    user_id = Column(
        Text,
        ForeignKey("User.id", ondelete="CASCADE"),
        nullable=False,
    )

    workspace_id = Column(
        Text,
        ForeignKey("Workspace.id", ondelete="CASCADE"),
        nullable=False,
    )

    __table_args__ = (UniqueConstraint("user_id", "workspace_id"),)
