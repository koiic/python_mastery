class BankAccount:
    """

    """

    def __init__(self, amount):
        self.balance = amount

    def withdraw(self, amount):
        if amount <= 0:
            return 'Invalid withdrawal amount'
        if amount > self.balance:
            return 'Insufficient Funds'
        else:
            self.balance = self.balance - amount
            return f'Your balance is ${self.balance}'

    def deposit(self, amount):
        if amount <= 0:
            return 'Invalid deposit amount'
        self.balance = self.balance + amount
        return f'Your new balance Is ${self.balance}'

    def get_balance(self):
        return f'Your balance Is ${self.balance}'

    def __eq__(self, other):
        if other.balance == self.balance:
            return True
        return False

    def __str__(self):
        return f'Your Bank Account Balance is ${self.balance}'


if __name__ == '__main__':
    account1 = BankAccount(100)
    print(account1.withdraw(101))
    print(account1.withdraw(10))
    print(account1.deposit(10000))
    print(account1.deposit(0))
    print(account1.get_balance())
    account2 = BankAccount(5000)
    print(account1.__eq__(account2))
