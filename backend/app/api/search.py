"""
Semantic search API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.schemas import SemanticSearchRequest, SemanticSearchResponse
from app.services.search_service import SearchService

router = APIRouter()
search_service = SearchService()


@router.post("/semantic", response_model=SemanticSearchResponse)
async def semantic_search(
    request: SemanticSearchRequest,
    db: Session = Depends(get_db),
):
    """
    Perform semantic search across tasks and notes
    
    - **query**: Search query (natural language)
    - **entity_type**: Filter by 'task', 'note', or 'all' (default: 'all')
    - **limit**: Maximum number of results (default: 10, max: 100)
    """
    try:
        results = await search_service.semantic_search(
            db,
            request.query,
            request.entity_type,
            request.limit,
        )
        return SemanticSearchResponse(
            results=results,
            query=request.query,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

