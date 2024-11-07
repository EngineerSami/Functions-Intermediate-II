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

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")


user1 = User("Sami Daraghmeh")
user1.make_deposit(500)
user1.display_user_balance() 
user1.make_withdrawal(200)
user1.display_user_balance() 
