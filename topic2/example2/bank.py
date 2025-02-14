# Topic 2 - Code coverage can be misleading
class Account:
    def __init__(self, balance):
        self.balance = balance

    def transfer(self, amount, other):
        self.balance -= amount
        other.balance += amount
