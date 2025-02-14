import pytest
from topic1.good.profit import profit


def test_profit():
    assert profit(50, 10) == 40
