from database import Base, engine
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())


class UUIDMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)


class User(Base, TimestampMixin, UUIDMixin):
    __table_args__ = {'schema': 'content'}
    __tablename__ = 'users'

    username = Column(String(length=25), nullable=False)
    email = Column(String(length=255), unique=True, nullable=False)
    password = Column(String(length=255), nullable=False)


class Username(Base, TimestampMixin, UUIDMixin):
    __table_args__ = {'schema': 'content'}
    __tablename__ = 'usernames'

    username = Column(String(length=255), nullable=False, unique=True)
    taken = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
