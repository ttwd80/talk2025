import pytest
from topic1.great.profit import profit


def test_profit_again():
    assert profit(50, 10) == 40
    assert profit(25, 5) == 20
