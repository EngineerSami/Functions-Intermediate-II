class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"Deposit of ${amount} accepted. Current balance: ${self.account_balance}")
        return self

    def make_withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrawal of ${amount} accepted. Current balance: ${self.account_balance}")
        else:
            print("Insufficient funds.")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            other_user.account_balance += amount
            print(f"{self.name} transferred ${amount} to {other_user.name}")
        else:
            print("Insufficient funds.")
        return self


user1 = User("Guido van Rossum", "guido@python.org")
user2 = User("Grace Hopper", "grace@ada.com")
user3 = User("Alan Turing", "alan@enigma.net")


user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


user2.make_deposit(500).make_deposit(100).make_withdrawal(200).make_withdrawal(150).display_user_balance()


user3.make_deposit(250).make_withdrawal(100).make_withdrawal(50).make_withdrawal(75).display_user_balance()


