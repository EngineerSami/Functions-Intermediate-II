class BankAccount:
    def __init__(self, int_rate=1, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount(0.05)
account2 = BankAccount(0.03)

account1.deposit(100).deposit(50).deposit(25).withdraw(30).yield_interest().display_account_info()
account2.deposit(200).deposit(100).withdraw(50).withdraw(75).withdraw(30).withdraw(20).yield_interest().display_account_info()
