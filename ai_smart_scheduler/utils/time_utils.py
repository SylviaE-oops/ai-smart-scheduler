"""Time utility functions."""

from __future__ import annotations


def time_to_minutes(time_str: str) -> int:
    """Convert 'HH:MM' string to total minutes since midnight.

    Args:
        time_str: Time in 'HH:MM' format.

    Returns:
        Total minutes since midnight.

    Raises:
        ValueError: If the format is invalid.
    """
    try:
        hours, minutes = map(int, time_str.split(":"))
    except (ValueError, AttributeError) as exc:
        raise ValueError(f"Invalid time format '{time_str}'. Expected 'HH:MM'.") from exc
    return hours * 60 + minutes


def minutes_to_time(minutes: int) -> str:
    """Convert total minutes since midnight to 'HH:MM' string.

    Args:
        minutes: Total minutes since midnight (0–1439).

    Returns:
        Time string in 'HH:MM' format.
    """
    return f"{minutes // 60:02d}:{minutes % 60:02d}"
