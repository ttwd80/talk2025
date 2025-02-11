import pytest
from profit import profit

def test_profit():
    assert profit(60, 15) == 45
