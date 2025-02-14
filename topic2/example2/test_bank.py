import pytest
from topic2.example2.bank import Account

def test_account():
    seller = Account(100)
    buyer = Account(100)
    buyer.transfer(50, seller)
    assert seller.balance == 150
    assert buyer.balance == 50
