import abc
from abc import ABC


class BankAccount(ABC):

    @abc.abstractmethod
    def create_account(self):
        raise NotImplementedError


class PrintInformation(ABC):

    @abc.abstractmethod
    def render(self):
        raise NotImplementedError


class PrintInformationPersonalAccount(PrintInformation):
    def render(self):
        print("validate user identity")
        print("calculate interest rate")
        print("register Personal Account ")


class PrintInformationBusinessAccount(PrintInformation):
    def render(self):
        print("validate user identity")
        print("calculate interest rate")
        print("register Business Account ")


class PrintInformationSavingsAccount(PrintInformation):
    def render(self):
        print("validate user identity")
        print("calculate interest rate")
        print("register Savings Account ")


class PersonalAccount(BankAccount):

    def create_account(self) -> PrintInformationPersonalAccount:
        return PrintInformationPersonalAccount()


class BusinessAccount(BankAccount):

    def create_account(self) -> PrintInformationBusinessAccount:
        return PrintInformationBusinessAccount()


class SavingsAccount(BankAccount):

    def create_account(self) -> PrintInformationSavingsAccount:
        return PrintInformationSavingsAccount()


def account_factory(account):
    account_type = {
        "Personal": PersonalAccount,
        "Business": BusinessAccount,
        "Savings": SavingsAccount,
    }
    account = account_type.get(account)()
    create_account = account.create_account()
    create_account.render()


def main():
    account_type = input("Wybierz rodzaj konta [Personal, Business, Savings]: ")
    account_factory(account_type)


if __name__ == "__main__":
    main()
