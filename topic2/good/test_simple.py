import pytest
from topic2.good.simple import water


def test_water():
    assert water(-5) == "ice"
    assert water(20) == "water"
    assert water(120) == "steam"