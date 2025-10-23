"""
Note service for business logic
"""

from sqlalchemy.orm import Session
from app.models.models import Note
from app.schemas.schemas import NoteCreate, NoteUpdate
from app.services.embedding_service import EmbeddingService
from app.services.ai_service import AIService
from typing import Optional, List


class NoteService:
    """Service for note operations"""

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.ai_service = AIService()

    async def create_note(self, db: Session, note: NoteCreate) -> Note:
        """Create a new note"""
        # Generate embedding for semantic search
        embedding = await self.embedding_service.get_embedding(note.title)

        # Generate AI summary
        try:
            summary_result = await self.ai_service.summarize(note.content, max_points=5)
            summary = summary_result.summary
        except Exception:
            summary = None

        db_note = Note(
            title=note.title,
            content=note.content,
            summary=summary,
            category=note.category,
            tags=note.tags,
            embedding=embedding,
        )
        db.add(db_note)
        db.commit()
        db.refresh(db_note)
        return db_note

    async def list_notes(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        category: Optional[str] = None,
    ) -> List[Note]:
        """List notes with optional filtering"""
        query = db.query(Note)

        if category:
            query = query.filter(Note.category == category)

        return query.offset(skip).limit(limit).all()

    async def get_note(self, db: Session, note_id: str) -> Optional[Note]:
        """Get a specific note"""
        return db.query(Note).filter(Note.id == note_id).first()

    async def update_note(
        self, db: Session, note_id: str, note_update: NoteUpdate
    ) -> Optional[Note]:
        """Update a note"""
        db_note = db.query(Note).filter(Note.id == note_id).first()
        if not db_note:
            return None

        update_data = note_update.model_dump(exclude_unset=True)

        # Regenerate embedding if title or content changed
        if "title" in update_data or "content" in update_data:
            title = update_data.get("title", db_note.title)
            embedding = await self.embedding_service.get_embedding(title)
            update_data["embedding"] = embedding

            # Regenerate summary if content changed
            if "content" in update_data:
                try:
                    summary_result = await self.ai_service.summarize(
                        update_data["content"], max_points=5
                    )
                    update_data["summary"] = summary_result.summary
                except Exception:
                    pass

        for field, value in update_data.items():
            setattr(db_note, field, value)

        db.commit()
        db.refresh(db_note)
        return db_note

    async def delete_note(self, db: Session, note_id: str) -> bool:
        """Delete a note"""
        db_note = db.query(Note).filter(Note.id == note_id).first()
        if not db_note:
            return False

        db.delete(db_note)
        db.commit()
        return True

