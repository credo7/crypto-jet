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
    is_admin = Column(Boolean, default=False)

    def to_json(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.email,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
        }

    @staticmethod
    def to_json_list(users):
        return [user.to_json() for user in users]


class Username(Base, TimestampMixin, UUIDMixin):
    __table_args__ = {'schema': 'content'}
    __tablename__ = 'usernames'

    username = Column(String(length=255), nullable=False, unique=True)
    taken = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
