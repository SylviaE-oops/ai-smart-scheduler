"""Task model representing a schedulable unit of work."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class Priority(str, Enum):
    """Priority levels for tasks."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Task(BaseModel):
    """A task to be scheduled."""

    id: str = Field(description="Unique identifier for the task")
    title: str = Field(description="Short title of the task")
    description: str = Field(default="", description="Optional detailed description")
    duration_minutes: int = Field(ge=1, description="Estimated duration in minutes")
    priority: Priority = Field(default=Priority.MEDIUM, description="Task priority level")
    tags: list[str] = Field(default_factory=list, description="Optional tags for categorization")
    deadline: str | None = Field(default=None, description="Optional deadline (ISO 8601 date or datetime)")
