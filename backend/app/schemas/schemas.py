"""
Pydantic schemas for request/response validation
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class TaskBase(BaseModel):
    """Base task schema"""

    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: int = Field(default=0, ge=0, le=3)
    category: Optional[str] = None
    tags: List[str] = Field(default_factory=list)


class TaskCreate(TaskBase):
    """Schema for creating a task"""

    pass


class TaskUpdate(BaseModel):
    """Schema for updating a task"""

    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[int] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    completed: Optional[bool] = None


class TaskResponse(TaskBase):
    """Schema for task response"""

    id: str
    completed: bool
    ai_priority_score: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NoteBase(BaseModel):
    """Base note schema"""

    title: str = Field(..., min_length=1, max_length=255)
    content: str = Field(..., min_length=1)
    category: Optional[str] = None
    tags: List[str] = Field(default_factory=list)


class NoteCreate(NoteBase):
    """Schema for creating a note"""

    pass


class NoteUpdate(BaseModel):
    """Schema for updating a note"""

    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[List[str]] = None


class NoteResponse(NoteBase):
    """Schema for note response"""

    id: str
    summary: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SummarizeRequest(BaseModel):
    """Schema for summarization request"""

    content: str = Field(..., min_length=1)
    max_points: int = Field(default=5, ge=1, le=10)


class SummarizeResponse(BaseModel):
    """Schema for summarization response"""

    summary: str
    bullet_points: List[str]


class PrioritizeRequest(BaseModel):
    """Schema for task prioritization request"""

    tasks: List[TaskResponse]


class PrioritizeResponse(BaseModel):
    """Schema for task prioritization response"""

    prioritized_tasks: List[TaskResponse]
    next_best_action: Optional[TaskResponse] = None
    reasoning: str


class SemanticSearchRequest(BaseModel):
    """Schema for semantic search request"""

    query: str = Field(..., min_length=1)
    entity_type: str = Field(default="all")  # 'task', 'note', or 'all'
    limit: int = Field(default=10, ge=1, le=100)


class SemanticSearchResult(BaseModel):
    """Schema for semantic search result"""

    entity_type: str  # 'task' or 'note'
    entity_id: str
    title: str
    similarity_score: float
    content: Optional[str] = None


class SemanticSearchResponse(BaseModel):
    """Schema for semantic search response"""

    results: List[SemanticSearchResult]
    query: str

