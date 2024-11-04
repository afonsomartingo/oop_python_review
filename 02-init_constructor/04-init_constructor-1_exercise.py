'''
Problem Statement: "BankAccount Class"

You are tasked with creating a simple Python class to represent a bank account. The class should allow for the following actions:

Initializing a new account with a specified owner name and an initial balance.
Making deposits to add money to the account.
Making withdrawals to remove money from the account.
Printing the current balance of the account.
Requirements
Constructor (__init__ method):

The class BankAccount should have an __init__ method that accepts two parameters:
owner: a string that represents the account owner’s name.
initial_balance: an optional parameter (default is 0) that represents the starting balance of the account.
Initialize the owner and balance attributes with these values.
Methods:

deposit(self, amount): This method takes an amount parameter and adds it to the account’s balance. It should print a message showing the amount deposited and the new balance.
withdraw(self, amount): This method takes an amount parameter and subtracts it from the account’s balance. It should print a message showing the amount withdrawn and the new balance. If the amount is greater than the balance, it should print an "Insufficient funds" message and prevent the withdrawal.
get_balance(self): This method should return the current balance of the account.
'''

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def get_balance(self):
        return self.balance


if __name__ == "__main__":
    # Creating a new bank account
    my_account = BankAccount("Alice", 100)  # Initial balance of 100
    print(my_account.get_balance())          # Output should be 100

    # Making a deposit
    my_account.deposit(50)                   # Output: "Deposited 50. New balance: 150"

    # Making a withdrawal
    my_account.withdraw(30)                  # Output: "Withdrew 30. New balance: 120"
    my_account.withdraw(200)                 # Output: "Insufficient funds"

    print(my_account.get_balance())          # Output should be 120

