"""Core scheduler logic for AI Smart Scheduler."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ai_smart_scheduler.models.schedule import Schedule
    from ai_smart_scheduler.models.user import User


class Scheduler:
    """Generates personalized daily schedules using AI."""

    def __init__(self, user: "User") -> None:
        self.user = user

    def generate(self) -> "Schedule":
        """Generate a personalized schedule for the user."""
        from ai_smart_scheduler.ai.generator import ScheduleGenerator

        generator = ScheduleGenerator(self.user)
        return generator.generate()
