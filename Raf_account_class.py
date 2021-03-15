from exceptions import InsufficientFundsException

class Account:
    numCreated = 0
    def __init__(self,first_name, last_name, current):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = current
        Account.numCreated +=1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    def deposit(self, amount):
        self.balance += amount
        return

    def withdraw(self, amount):
        try:
        #     account.withdraw(5000)
        # except InsufficientFundsException:
        #     print(f'Insufficient funds for {account.name} to withdraw 5000')

            if self.balance - amount < 0:
                raise InsufficientFundsException
                pass
            else:
                self.balance -= amount

            print(f'{self.first_name} has withdrawn £{amount}')
            self.make_charges()

        except InsufficientFundsException:
            print(f'Insufficient funds for {self.first_name} to withdraw {amount}')


    def make_charges(self):
        # apply overdraft charges if below zero
        if self.balance < 0:
            self.balance -= 20
            print(f'{self.first_name} is overdrawn and have been charged £20')

    def get_balance(self):
        return self.balance

# class StudentAccount(Account):
#     def __init__(self, current, overdraft_amount=0):
#         super().__init__(current)
#         self.overdraft_amount = overdraft_amount
#     def set_student_overdraft(self, amount, overdraft=0):
#         self.withdraw(amount)
#         if self.balance < 0:
#             overdraft = (self.balance-amount)*(-1)
#
#             if overdraft >= 2000:
#                 print("you have reached your limit", overdraft)
#             else:
#                 print ('hello')
#
#         else:
#             overdraft==0


