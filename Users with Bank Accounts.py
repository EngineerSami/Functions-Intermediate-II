class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

user1 = User("Sami Daraghmeh")
user1.make_deposit(500).display_user_balance() .make_withdrawal(200).display_user_balance() 
