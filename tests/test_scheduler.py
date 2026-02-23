"""Tests for the Scheduler and ScheduleGenerator."""

from ai_smart_scheduler.models.task import Priority, Task
from ai_smart_scheduler.models.user import User
from ai_smart_scheduler.scheduler import Scheduler
from ai_smart_scheduler.ai.generator import ScheduleGenerator


def _make_user(**kwargs) -> User:
    return User(name="Test User", **kwargs)


def test_scheduler_generate_no_tasks():
    user = _make_user()
    scheduler = Scheduler(user)
    schedule = scheduler.generate()
    assert schedule.date is not None
    assert isinstance(schedule.blocks, list)


def test_schedule_generator_with_tasks():
    user = _make_user()
    tasks = [
        Task(id="t1", title="Deep Work", duration_minutes=90, priority=Priority.HIGH),
        Task(id="t2", title="Email", duration_minutes=30, priority=Priority.MEDIUM),
    ]
    generator = ScheduleGenerator(user, tasks=tasks)
    schedule = generator.generate(date="2026-02-23")
    assert schedule.date == "2026-02-23"
    titled = [b.label for b in schedule.blocks]
    assert "Deep Work" in titled


def test_schedule_generator_respects_work_hours():
    user = _make_user()
    tasks = [Task(id=f"t{i}", title=f"Task {i}", duration_minutes=600) for i in range(5)]
    generator = ScheduleGenerator(user, tasks=tasks)
    schedule = generator.generate(date="2026-02-23")
    for block in schedule.blocks:
        assert block.start_time >= user.constraints.work_start
        assert block.end_time <= user.constraints.work_end
