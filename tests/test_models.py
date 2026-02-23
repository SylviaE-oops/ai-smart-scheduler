"""Tests for data models."""

import pytest

from ai_smart_scheduler.models.task import Priority, Task
from ai_smart_scheduler.models.user import User, UserConstraints
from ai_smart_scheduler.models.schedule import Schedule, ScheduledBlock


def test_task_defaults():
    task = Task(id="t1", title="Write report", duration_minutes=60)
    assert task.priority == Priority.MEDIUM
    assert task.tags == []
    assert task.deadline is None


def test_task_priority():
    task = Task(id="t2", title="Fix bug", duration_minutes=30, priority=Priority.URGENT)
    assert task.priority == Priority.URGENT


def test_user_constraints_defaults():
    constraints = UserConstraints()
    assert constraints.work_start == "09:00"
    assert constraints.work_end == "17:00"
    assert constraints.break_duration_minutes == 15
    assert constraints.max_focus_block_minutes == 90


def test_user_creation():
    user = User(name="Alice", priorities=["deep work"], personality_traits=["morning person"])
    assert user.name == "Alice"
    assert "deep work" in user.priorities
    assert isinstance(user.constraints, UserConstraints)


def test_schedule_creation():
    task = Task(id="t1", title="Planning", duration_minutes=30)
    block = ScheduledBlock(start_time="09:00", end_time="09:30", task=task, label="Planning")
    schedule = Schedule(date="2026-02-23", blocks=[block])
    assert schedule.date == "2026-02-23"
    assert len(schedule.blocks) == 1
    assert schedule.blocks[0].task.title == "Planning"
