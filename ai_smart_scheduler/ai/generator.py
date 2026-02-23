"""AI-powered schedule generator."""

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from ai_smart_scheduler.models.schedule import Schedule, ScheduledBlock
from ai_smart_scheduler.models.task import Task
from ai_smart_scheduler.utils.time_utils import minutes_to_time, time_to_minutes

if TYPE_CHECKING:
    from ai_smart_scheduler.models.user import User


class ScheduleGenerator:
    """Generates a personalized daily schedule for a user using AI."""

    def __init__(self, user: "User", tasks: list[Task] | None = None) -> None:
        self.user = user
        self.tasks: list[Task] = tasks or []

    def generate(self, date: str | None = None) -> Schedule:
        """Generate a schedule for the given date (defaults to today).

        This is a stub implementation. Override or extend with AI provider
        integration (e.g. OpenAI) to produce intelligent schedules.
        """
        if date is None:
            date = datetime.date.today().isoformat()

        blocks: list[ScheduledBlock] = []
        current_minutes = time_to_minutes(self.user.constraints.work_start)
        end_minutes = time_to_minutes(self.user.constraints.work_end)

        for task in self.tasks:
            if current_minutes + task.duration_minutes > end_minutes:
                break
            start = minutes_to_time(current_minutes)
            current_minutes += task.duration_minutes
            end = minutes_to_time(current_minutes)
            blocks.append(ScheduledBlock(start_time=start, end_time=end, task=task, label=task.title))

            break_duration = self.user.constraints.break_duration_minutes
            if break_duration > 0 and current_minutes + break_duration <= end_minutes:
                break_start = minutes_to_time(current_minutes)
                current_minutes += break_duration
                break_end = minutes_to_time(current_minutes)
                blocks.append(ScheduledBlock(start_time=break_start, end_time=break_end, label="Break"))

        return Schedule(date=date, blocks=blocks)
