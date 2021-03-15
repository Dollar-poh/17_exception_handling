from datetime import date
from Raf_account_class import Account
from Raf_age_exception import AgeRestrictionError

class ChildBankAccount(Account):
    def __init__(self, first_name, last_name, current, restricted=True):
        super().__init__(first_name, last_name, current)
        self.balance = current
        self.restricted = restricted

    def calculate_age(self, dtob):
        today = date.today()
        return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))


    def isRestricted(self, dtob):
        # today = date.today()
        # born_year = print((input("Please enter your birth year"))
        # birth_year = int(born_year)
        # age = today.year - birth_year
        try:
            if self.calculate_age(dtob)<18:
                print("Restrictions on account is permitted")
            else:
                raise AgeRestrictionError
        except AgeRestrictionError:
            print("{}".format(dtob), "on restricted account is not permitted")
