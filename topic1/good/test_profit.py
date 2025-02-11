import pytest
from topic1.good.profit import profit


def test_profit():
    assert profit(60, 15) == 45
