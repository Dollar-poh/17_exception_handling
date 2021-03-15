from Raf_account_class import Account
from Raf_Child_Bank_Account_Class import ChildBankAccount
from Raf_savings_account_class import SavingsAccount
from datetime import date

Sanele_account = Account("Sanele", "Evanson", 1000000)
print(Sanele_account.fullname)
Sanele_account.first_name = "Lily"
print(Sanele_account.first_name)
print(Sanele_account.email)


Raf_account = ChildBankAccount("Raf", "Atkinson", 150000)
print(Raf_account.get_balance())

# print(Raf_account.restricted)

Raf_account.isRestricted(date(2004, 3, 11))
# Raf_account.restricted(date(1991, 3, 11))

Eve_Account = ChildBankAccount("Eve", "Bob", 30000)
Eve_Account.isRestricted(date(1991, 3, 11))