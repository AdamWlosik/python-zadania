import abc
from abc import ABC


class BankAccount(ABC):

    def __init__(self, account_type):
        self.account_type = account_type

    @abc.abstractmethod
    def validate_user_identity(self):
        raise NotImplementedError

    @abc.abstractmethod
    def calculate_interest_rate(self):
        raise NotImplementedError

    @abc.abstractmethod
    def register_account(self):
        raise NotImplementedError


class PersonalAccount(BankAccount):

    def __init__(self):
        super().__init__("Personal Account")
        self.validate_user_identity()
        self.calculate_interest_rate()
        self.register_account()

    def validate_user_identity(self):
        print("validate user identity")

    def calculate_interest_rate(self):
        print("calculate interest rate")

    def register_account(self):
        print(f"register {self.account_type} ")


class BusinessAccount(BankAccount):

    def __init__(self):
        super().__init__("Business Account")
        self.validate_user_identity()
        self.calculate_interest_rate()
        self.register_account()

    def validate_user_identity(self):
        print("validate user identity")

    def calculate_interest_rate(self):
        print("calculate interest rate")

    def register_account(self):
        print(f"register {self.account_type} ")


class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__("Savings Account")
        self.validate_user_identity()
        self.calculate_interest_rate()
        self.register_account()

    def validate_user_identity(self):
        print("validate user identity")

    def calculate_interest_rate(self):
        print("calculate interest rate")

    def register_account(self):
        print(f"register {self.account_type} ")


def account_factory(account):
    account_type = {
        "Personal": PersonalAccount,
        "Business": BusinessAccount,
        "Savings": SavingsAccount,
    }
    account_type.get(account)()
    """if account == "Personal":
        return PersonalAccount()
    elif account == "Business":
        return BusinessAccount()
    elif account == "Savings":
        return SavingsAccount()"""


def main():
    account_type = input("Wybierz rodzaj konta [Personal, Business, Savings]: ")
    account_factory(account_type)


if __name__ == "__main__":
    main()
