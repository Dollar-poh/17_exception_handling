from Raf_account_class import Account, SavingsAccount, ChildBankAccount
from datetime import date

Sanele_account = Account(1000000)
# Evian_account = Account(-6)
# print(Evian_account.get_balance())
Sanele_account.deposit(20000)
Sanele_account.get_balance()

print(Sanele_account.get_balance())

Rafika_account = SavingsAccount(2000000)
Rafika_account.withdraw(30000)
print(Rafika_account.get_balance())

Rafika_account.add_interest(2400)
print(Rafika_account.get_balance())

Rafika_account.deduct_withdrawal(2500)
print(Rafika_account.get_balance())

# student1_account = StudentAccount(current=1300)
# student1_account.set_student_overdraft(amount=2000)
# print(student1_account.get_balance())

kid1_account = ChildBankAccount(41000)
print(kid1_account.calculate_age(date(1991, 3, 11)))
kid1_account.isRestricted(date(1991, 3, 11))
print(kid1_account.isRestricted(date(1991, 3, 11)))