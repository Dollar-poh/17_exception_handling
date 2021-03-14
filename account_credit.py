from account import Account


class AccountCredit(Account):
    def __init__(self, name, age, ni_number, address):
        super().__init__(name, age, 0, ni_number, address)
        self.interest_rate = 0.5

    def add_monthly_interest(self):
        interest = -self.interest_rate * self._balance
        print(f'{interest} interest accrued this month')
        self._balance -= interest

    def withdraw(self, amount):
        self._balance -= amount
        print(f'{self.name} has withdrawn £{amount}')

    def get_balance(self):
        return -self._balance
