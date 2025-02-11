import pytest
from topic1.great.profit import profit


def test_profit():
    assert profit(16, 14) == 2
    assert profit(60, 15) == 45
