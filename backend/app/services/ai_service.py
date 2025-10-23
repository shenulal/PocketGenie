"""
AI service for LLM integration and task prioritization
"""

import requests
from typing import List, Optional
from app.core.config import settings
from app.schemas.schemas import (
    SummarizeResponse,
    PrioritizeResponse,
    TaskResponse,
)


class AIService:
    """Service for AI/LLM operations"""

    def __init__(self):
        self.zephyr_url = settings.ZEPHYR_API_URL

    async def summarize(self, content: str, max_points: int = 5) -> SummarizeResponse:
        """
        Summarize content using Z.ai LLM
        
        Args:
            content: Text to summarize
            max_points: Maximum bullet points
            
        Returns:
            SummarizeResponse with summary and bullet points
        """
        prompt = f"""Summarize the following content into {max_points} concise bullet points highlighting key information and tasks:

{content}

Provide the summary as a single paragraph, then list the bullet points."""

        try:
            # Try to call Z.ai server
            response = requests.post(
                f"{self.zephyr_url}/v1/completions",
                json={
                    "prompt": prompt,
                    "max_tokens": 500,
                    "temperature": 0.7,
                },
                timeout=30,
            )
            response.raise_for_status()
            result = response.json()
            text = result.get("choices", [{}])[0].get("text", "")
        except Exception as e:
            # Fallback: simple summarization
            print(f"Warning: Could not reach Z.ai server: {e}")
            text = self._simple_summarize(content, max_points)

        # Parse response into summary and bullet points
        lines = text.strip().split("\n")
        summary = lines[0] if lines else content[:200]

        bullet_points = []
        for line in lines[1:]:
            line = line.strip()
            if line and (line.startswith("-") or line.startswith("•") or line.startswith("*")):
                bullet_points.append(line.lstrip("-•* "))

        # Ensure we have bullet points
        if not bullet_points:
            bullet_points = [content[i : i + 100] for i in range(0, min(len(content), 500), 100)][:max_points]

        return SummarizeResponse(
            summary=summary,
            bullet_points=bullet_points[:max_points],
        )

    async def prioritize_tasks(self, tasks: List[TaskResponse]) -> PrioritizeResponse:
        """
        Prioritize tasks using AI
        
        Args:
            tasks: List of tasks to prioritize
            
        Returns:
            PrioritizeResponse with prioritized tasks and next best action
        """
        if not tasks:
            return PrioritizeResponse(
                prioritized_tasks=[],
                next_best_action=None,
                reasoning="No tasks to prioritize",
            )

        # Format tasks for prompt
        tasks_text = "\n".join(
            [
                f"- {t.title} (Priority: {t.priority}, Due: {t.due_date or 'No due date'})"
                for t in tasks
            ]
        )

        prompt = f"""Given the following tasks, rank them by urgency and recommend the next best task to focus on:

{tasks_text}

Consider:
1. Due dates (urgent deadlines first)
2. Priority levels
3. Task descriptions and complexity
4. Dependencies

Provide your analysis and recommendation."""

        try:
            # Try to call Z.ai server
            response = requests.post(
                f"{self.zephyr_url}/v1/completions",
                json={
                    "prompt": prompt,
                    "max_tokens": 500,
                    "temperature": 0.7,
                },
                timeout=30,
            )
            response.raise_for_status()
            result = response.json()
            reasoning = result.get("choices", [{}])[0].get("text", "")
        except Exception as e:
            # Fallback: simple prioritization
            print(f"Warning: Could not reach Z.ai server: {e}")
            reasoning = "Prioritized by due date and priority level"

        # Sort tasks by priority and due date
        prioritized = sorted(
            tasks,
            key=lambda t: (
                t.due_date is None,  # Tasks with due dates first
                t.due_date or "",  # Then by due date
                -t.priority,  # Then by priority (descending)
            ),
        )

        next_best = prioritized[0] if prioritized else None

        return PrioritizeResponse(
            prioritized_tasks=prioritized,
            next_best_action=next_best,
            reasoning=reasoning,
        )

    def _simple_summarize(self, content: str, max_points: int) -> str:
        """Simple fallback summarization"""
        sentences = content.split(".")
        summary = ". ".join(sentences[:2]) + "."

        bullet_points = []
        for i, sentence in enumerate(sentences[2:]):
            if i >= max_points:
                break
            sentence = sentence.strip()
            if sentence:
                bullet_points.append(f"- {sentence}")

        return summary + "\n" + "\n".join(bullet_points)

