"""
Search service for semantic search
"""

from sqlalchemy.orm import Session
from typing import List
from app.models.models import Task, Note
from app.schemas.schemas import SemanticSearchResult
from app.services.embedding_service import EmbeddingService


class SearchService:
    """Service for semantic search operations"""

    def __init__(self):
        self.embedding_service = EmbeddingService()

    async def semantic_search(
        self,
        db: Session,
        query: str,
        entity_type: str = "all",
        limit: int = 10,
    ) -> List[SemanticSearchResult]:
        """
        Perform semantic search across tasks and notes
        
        Args:
            db: Database session
            query: Search query
            entity_type: 'task', 'note', or 'all'
            limit: Maximum results
            
        Returns:
            List of search results sorted by similarity
        """
        # Generate embedding for query
        query_embedding = await self.embedding_service.get_embedding(query)

        if not query_embedding:
            return []

        results = []

        # Search tasks
        if entity_type in ["task", "all"]:
            tasks = db.query(Task).all()
            for task in tasks:
                if task.embedding:
                    similarity = await self.embedding_service.similarity(
                        query_embedding, task.embedding
                    )
                    if similarity > 0.3:  # Threshold
                        results.append(
                            SemanticSearchResult(
                                entity_type="task",
                                entity_id=task.id,
                                title=task.title,
                                similarity_score=similarity,
                                content=task.description,
                            )
                        )

        # Search notes
        if entity_type in ["note", "all"]:
            notes = db.query(Note).all()
            for note in notes:
                if note.embedding:
                    similarity = await self.embedding_service.similarity(
                        query_embedding, note.embedding
                    )
                    if similarity > 0.3:  # Threshold
                        results.append(
                            SemanticSearchResult(
                                entity_type="note",
                                entity_id=note.id,
                                title=note.title,
                                similarity_score=similarity,
                                content=note.content[:200],  # Truncate for response
                            )
                        )

        # Sort by similarity score (descending)
        results.sort(key=lambda x: x.similarity_score, reverse=True)

        return results[:limit]

