from account import Account
from account_savings import AccountSavings
from account_credit import AccountCredit
from account_child import AccountChild
from exceptions import InsufficientFundsException



account = Account('Alice', 25, 1000, 'SV182945B', 'Sample address')
print(f'Account {account.account_number} belongs to {account.name}')
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.deposit(100)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.withdraw(1200)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.deposit(500)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
print('---------------------------------------------------------')

account = AccountSavings('Bob', 25, 1000, 'SV182945C', 'Sample address 2')
print(f'Account {account.account_number} belongs to {account.name}')
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.deposit(100)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.withdraw(1200)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.deposit(500)
account.add_monthly_interest()
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
print('---------------------------------------------------------')

account = AccountCredit('Charlie', 25, 'SV182945D', 'Sample address 3')
print(f'Account {account.account_number} belongs to {account.name}')
account.withdraw(1200)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.add_monthly_interest()
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
print('---------------------------------------------------------')

account = AccountChild('David', 18, 1000, 'SV182945D', 'Sample address 4')
account.withdraw(100)
account = account.turn_adult()
account.withdraw(100)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
print('---------------------------------------------------------')

account = Account('Erik', 25, 1000, 'SV182945E', 'Sample address 5')
print(f'Account {account.account_number} belongs to {account.name}')
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.deposit(100)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
account.withdraw(2200)
balance = account.get_balance()
print(f'{account.name} has balance of £{balance}')
# try:
#     account.withdraw(5000)
# except InsufficientFundsException:
#     print(f'Insufficient funds for {account.name} to withdraw 5000')
