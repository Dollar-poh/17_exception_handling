from exceptions import InsufficientFundsException


class Account:
    num_created = 0

    def __init__(self, name, age, initial_balance, ni_number, address):
        Account.num_created += 1
        self.account_number = f'{Account.num_created:08}'
        self.name = name
        self.age = age
        self._balance = initial_balance
        self._ni_number = ni_number
        self._address = address

    def deposit(self, amount):
        self._balance += amount
        print(f'{self.name} has deposited £{amount}')

    def withdraw(self, amount):
        try:
        #     account.withdraw(5000)
        # except InsufficientFundsException:
        #     print(f'Insufficient funds for {account.name} to withdraw 5000')

            if self._balance - amount < 0:
                raise InsufficientFundsException
                pass
            else:
                self._balance -= amount

            print(f'{self.name} has withdrawn £{amount}')
            self.make_charges()

        except InsufficientFundsException:
            print(f'Insufficient funds for {self.name} to withdraw {amount}')


    def make_charges(self):
        # apply overdraft charges if below zero
        if self._balance < 0:
            self._balance -= 20
            print(f'{self.name} is overdrawn and have been charged £20')

    def get_balance(self):
        return self._balance
