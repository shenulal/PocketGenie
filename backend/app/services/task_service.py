"""
Task service for business logic
"""

from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.models import Task
from app.schemas.schemas import TaskCreate, TaskUpdate
from app.services.embedding_service import EmbeddingService
from typing import Optional, List


class TaskService:
    """Service for task operations"""

    def __init__(self):
        self.embedding_service = EmbeddingService()

    async def create_task(self, db: Session, task: TaskCreate) -> Task:
        """Create a new task"""
        # Generate embedding for semantic search
        embedding = await self.embedding_service.get_embedding(task.title)

        db_task = Task(
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            priority=task.priority,
            category=task.category,
            tags=task.tags,
            embedding=embedding,
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    async def list_tasks(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        completed: Optional[bool] = None,
        category: Optional[str] = None,
    ) -> List[Task]:
        """List tasks with optional filtering"""
        query = db.query(Task)

        if completed is not None:
            query = query.filter(Task.completed == completed)

        if category:
            query = query.filter(Task.category == category)

        return query.offset(skip).limit(limit).all()

    async def get_task(self, db: Session, task_id: str) -> Optional[Task]:
        """Get a specific task"""
        return db.query(Task).filter(Task.id == task_id).first()

    async def update_task(
        self, db: Session, task_id: str, task_update: TaskUpdate
    ) -> Optional[Task]:
        """Update a task"""
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if not db_task:
            return None

        update_data = task_update.model_dump(exclude_unset=True)

        # Regenerate embedding if title or description changed
        if "title" in update_data or "description" in update_data:
            title = update_data.get("title", db_task.title)
            embedding = await self.embedding_service.get_embedding(title)
            update_data["embedding"] = embedding

        for field, value in update_data.items():
            setattr(db_task, field, value)

        db.commit()
        db.refresh(db_task)
        return db_task

    async def delete_task(self, db: Session, task_id: str) -> bool:
        """Delete a task"""
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if not db_task:
            return False

        db.delete(db_task)
        db.commit()
        return True

    async def complete_task(self, db: Session, task_id: str) -> Optional[Task]:
        """Mark a task as completed"""
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if not db_task:
            return None

        db_task.completed = True
        db.commit()
        db.refresh(db_task)
        return db_task

