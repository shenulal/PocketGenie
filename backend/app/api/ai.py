"""
AI/LLM API endpoints
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.schemas import (
    SummarizeRequest,
    SummarizeResponse,
    PrioritizeRequest,
    PrioritizeResponse,
    TaskResponse,
)
from app.services.ai_service import AIService

router = APIRouter()
ai_service = AIService()


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_content(
    request: SummarizeRequest,
):
    """
    Summarize content using AI
    
    - **content**: Text content to summarize
    - **max_points**: Maximum bullet points (default: 5, max: 10)
    """
    try:
        result = await ai_service.summarize(request.content, request.max_points)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/prioritize", response_model=PrioritizeResponse)
async def prioritize_tasks(
    request: PrioritizeRequest,
    db: Session = Depends(get_db),
):
    """
    Prioritize tasks using AI
    
    Analyzes tasks based on:
    - Due dates
    - Priority levels
    - Task descriptions
    - Urgency indicators
    
    Returns prioritized list and "Next Best Action" recommendation
    """
    try:
        result = await ai_service.prioritize_tasks(request.tasks)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

