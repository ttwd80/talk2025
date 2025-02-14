import pytest
from topic2.example1.liquid import water

def test_water():
    assert water(-5) == "ice"
    assert water(20) == "water"
