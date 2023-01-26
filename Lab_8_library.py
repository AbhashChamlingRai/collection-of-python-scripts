class BankAccount:
    __all_accounts = [] # Storing all accounts in a list
    def __init__(self, balance: float, acc_number: int):
        self.__balance = balance
        self.__acc_number = acc_number
        BankAccount.__all_accounts.append(self)
    
    def get_account(self) -> int:
        return self.__acc_number

    def get_balance(self) -> float:
        print(f"\nAccount {self.get_account()} -> Your balance is '{self.__balance}'")
        return self.__balance

    def deposit(self, amount: float):
        self.__balance += amount
        print(f"\nAccount {self.get_account()} -> Deposit of {amount} successful. Your current balance is '{self.__balance}'")

    def withdraw(self, amount: float):
        self.__balance -= amount
        print(f"\nAccount {self.get_account()} -> Withdraw of {amount} successful. Your current balance is '{self.__balance}'")

    def transfer(self, amount: float, acc: int):
        self.__balance -= amount

        for account in BankAccount.__all_accounts:
            if account.get_account() == acc:
                account.deposit(amount)
                print(f"\nAccount {self.get_account()} -> Transfer of {amount} to account {account.get_account()} successful.")