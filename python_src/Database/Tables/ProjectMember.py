from sqlalchemy import *
from sqlalchemy.dialects.postgresql import JSONB, ENUM
from sqlalchemy.sql import expression, func
from sqlalchemy.schema import UniqueConstraint

from ..Base import Base


class ProjectMember(Base):
    __tablename__ = "ProjectMember"

    id = Column(Text, primary_key=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False)

    role = Column(Text, nullable=False)

    user_id = Column(
        Text,
        ForeignKey("User.id", ondelete="CASCADE"),
        nullable=False,
    )

    project_id = Column(
        Text,
        ForeignKey("Project.id", ondelete="CASCADE"),
        nullable=False,
    )

    __table_args__ = (UniqueConstraint("user_id", "project_id"),)
