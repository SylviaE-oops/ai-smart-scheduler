"""Schedule model representing a generated daily schedule."""

from __future__ import annotations

from pydantic import BaseModel, Field

from ai_smart_scheduler.models.task import Task


class ScheduledBlock(BaseModel):
    """A time block within the schedule."""

    start_time: str = Field(description="Block start time (HH:MM)")
    end_time: str = Field(description="Block end time (HH:MM)")
    task: Task | None = Field(default=None, description="Task assigned to this block, or None for a break")
    label: str = Field(default="", description="Human-readable label (e.g. 'Break', 'Lunch')")


class Schedule(BaseModel):
    """A complete daily schedule."""

    date: str = Field(description="Schedule date (ISO 8601 format, e.g. 2026-02-23)")
    blocks: list[ScheduledBlock] = Field(default_factory=list, description="Ordered list of time blocks")
    notes: str = Field(default="", description="AI-generated notes or explanations for the schedule")
