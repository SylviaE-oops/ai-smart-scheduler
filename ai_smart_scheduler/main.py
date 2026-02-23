"""Entry point for the AI Smart Scheduler."""

from ai_smart_scheduler.models.user import User
from ai_smart_scheduler.models.task import Task
from ai_smart_scheduler.scheduler import Scheduler


def main() -> None:
    """Run the AI Smart Scheduler CLI."""
    print("AI Smart Scheduler")
    print("==================")
    print("Generating your personalized daily schedule...")


if __name__ == "__main__":
    main()
