"""Tests for time utility functions."""

import pytest

from ai_smart_scheduler.utils.time_utils import minutes_to_time, time_to_minutes


def test_time_to_minutes_basic():
    assert time_to_minutes("09:00") == 540
    assert time_to_minutes("17:30") == 1050
    assert time_to_minutes("00:00") == 0
    assert time_to_minutes("23:59") == 1439


def test_time_to_minutes_invalid():
    with pytest.raises(ValueError):
        time_to_minutes("9:00am")
    with pytest.raises(ValueError):
        time_to_minutes("invalid")


def test_minutes_to_time_basic():
    assert minutes_to_time(540) == "09:00"
    assert minutes_to_time(1050) == "17:30"
    assert minutes_to_time(0) == "00:00"
    assert minutes_to_time(1439) == "23:59"


def test_roundtrip():
    for t in ("00:00", "09:00", "12:30", "23:59"):
        assert minutes_to_time(time_to_minutes(t)) == t
