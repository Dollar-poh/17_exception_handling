from account import Account


class AccountSavings(Account):
    def __init__(self, name, age, initial_balance, ni_number, address):
        super().__init__(name, age, initial_balance, ni_number, address)
        self.interest_rate = 0.36

    def add_monthly_interest(self):
        interest = self.interest_rate * self._balance
        print(f'{interest} interest earned this month')
        self._balance += interest
