from account import Account


class AccountChild(Account):
    def __init__(self, name, age, initial_balance, ni_number, address):
        super().__init__(name, age, initial_balance, ni_number, address)

    def withdraw(self, amount):
        print('Cant withdraw from child account')

    def turn_adult(self):
        if self.age >= 18:
            return Account(self.name, self.age, self._balance, self._ni_number, self._address)
