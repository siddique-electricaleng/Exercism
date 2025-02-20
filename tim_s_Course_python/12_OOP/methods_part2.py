import datetime
import pytz

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
        else:
            print("The amount deposited must be greater than 0")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print("You can only withdraw amount greater than 0 and less than or equal to account balance")
        self.show_balance()

    def show_balance(self):
        print(f"{self.name}'s Current Balance is {self.balance:.2f}")
if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()
    tim.deposit(1000)
    tim.withdraw(500)
    tim.withdraw(2000)