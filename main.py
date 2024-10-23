class BankAccount:
    def __init__(self, account_balance=1000):
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be greater than 0"
        self.__account_balance += amount
        return f'deposited {amount}'

    def withdraw(self, amount):
        if amount <= 0:
            return "amount must be greater than 0"
        if amount > self.__account_balance:
            return "Insufficient balance"
        self.__account_balance -= amount
        return f'withdrew {amount}'

    def check_balance(self):
        return f'Your account balance is {self.__account_balance}'

bank = BankAccount()
dep_amt = float(input("Enter the amount you want to deposit "))
with_amt = float(input("Enter the amount to withdraw "))
print(bank.deposit(dep_amt))
print(bank.withdraw(with_amt))
print(bank.check_balance())
