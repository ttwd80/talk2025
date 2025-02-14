import pytest
from topic1.profit import profit


def test_profit():
    assert profit(50, 10) == 40
