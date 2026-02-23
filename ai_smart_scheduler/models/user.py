"""User model representing preferences, personality, and constraints."""

from __future__ import annotations

from pydantic import BaseModel, Field


class UserConstraints(BaseModel):
    """Hard constraints that must be respected when generating a schedule."""

    work_start: str = Field(default="09:00", description="Earliest work start time (HH:MM)")
    work_end: str = Field(default="17:00", description="Latest work end time (HH:MM)")
    break_duration_minutes: int = Field(default=15, ge=0, description="Minimum break duration in minutes")
    max_focus_block_minutes: int = Field(default=90, ge=15, description="Max continuous focus block in minutes")


class User(BaseModel):
    """A user of the AI Smart Scheduler."""

    name: str = Field(description="User's full name")
    priorities: list[str] = Field(
        default_factory=list,
        description="Ordered list of user's top priorities (e.g. 'deep work', 'exercise')",
    )
    personality_traits: list[str] = Field(
        default_factory=list,
        description="Personality traits that influence scheduling (e.g. 'morning person', 'introvert')",
    )
    constraints: UserConstraints = Field(
        default_factory=UserConstraints,
        description="Hard scheduling constraints for the user",
    )
