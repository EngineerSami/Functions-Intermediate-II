class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}. New balance: {self.balance}")
        return self

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal: {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance}")
        return self

guido = User("Guido van Rossum")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
