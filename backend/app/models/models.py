"""
SQLAlchemy models for PocketGenie
"""

from sqlalchemy import Column, String, Text, DateTime, Integer, Float, JSON, Boolean
from sqlalchemy.sql import func
from app.core.database import Base
import uuid


class Task(Base):
    """Task model"""

    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(Integer, default=0)  # 0=low, 1=medium, 2=high, 3=urgent
    category = Column(String(100), nullable=True)
    tags = Column(JSON, default=list)  # List of tags
    completed = Column(Boolean, default=False)
    ai_priority_score = Column(Float, nullable=True)  # AI-generated priority
    embedding = Column(JSON, nullable=True)  # Vector embedding for semantic search
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"


class Note(Base):
    """Note model"""

    __tablename__ = "notes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text, nullable=True)  # AI-generated summary
    category = Column(String(100), nullable=True)
    tags = Column(JSON, default=list)  # List of tags
    embedding = Column(JSON, nullable=True)  # Vector embedding for semantic search
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Note {self.id}: {self.title}>"


class User(Base):
    """User model for multi-device sync"""

    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    preferences = Column(JSON, default=dict)  # User preferences
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<User {self.username}>"


class DeviceSyncLog(Base):
    """Device sync log for tracking multi-device synchronization"""

    __tablename__ = "device_sync_logs"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False)
    device_id = Column(String, nullable=False)
    entity_type = Column(String(50), nullable=False)  # 'task' or 'note'
    entity_id = Column(String, nullable=False)
    action = Column(String(50), nullable=False)  # 'create', 'update', 'delete'
    synced_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<DeviceSyncLog {self.id}>"

