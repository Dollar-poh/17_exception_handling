from Raf_account_class import Account

class SavingsAccount(Account):
    withdrawal_charge = 0.7
    interest_1 = 0.5

# The below constructor is not needed as we do not
# have any additional attributes - all is inherited
    # def __init__(self, current):
    #     pass

# Adding Methods
# This method adds interest with each deposit
    def add_interest(self, amount):
        return Account.deposit(self, amount*self.interest_1)

    # This method fines the user for withdrawals by deducting 70% of the withdrawal amount
    # each time the user withdraws
    def deduct_withdrawal(self, amount):
        return Account.withdraw(self, amount+(amount*self.withdrawal_charge))