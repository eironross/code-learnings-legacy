from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from typing import Optional
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR

class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column (
        INTEGER,
        nullable=False,
        primary_key=True,
        index=True,
        unique=True,
        comment="user key for users table"
    )
    
    name: Mapped[str] = mapped_column(
        VARCHAR(255),
        nullable=False,
        primary_key=False,
        comment="Name of the user"
    )