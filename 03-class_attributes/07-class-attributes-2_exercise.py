'''Problem Statement
Problem Name: BankAccount Class Attributes

Description:
You are creating a BankAccount class to manage basic bank accounts. The bank has a general interest rate applied to all accounts by default. However, each account holder can request a different interest rate for their individual account.

Define the BankAccount class with the following:

A class attribute default_interest_rate set to 0.03 (3%).
An instance attribute balance initialized by the constructor.
The class should include the following methods:

__init__(self, balance): Initializes the account with a given balance and sets an instance attribute interest_rate equal to default_interest_rate.
apply_interest(self): Updates the balance by adding the interest calculated using the interest_rate attribute. This method should use the account's 
specific interest_rate, whether it’s the default class rate or an overridden instance rate.

Override the interest_rate attribute for a specific account by setting a new rate as an instance attribute.

Delete the instance attribute interest_rate and verify that the account reverts to using the default_interest_rate.'''

class BankAccount:
    default_interest_rate = 0.03  # Class-level attribute

    def __init__(self, balance):
        self.bal = balance
        self.interest_rate = BankAccount.default_interest_rate  # Set instance-level interest rate

    def apply_interest(self):
        # Use instance-level interest_rate if it exists, otherwise fall back to class-level default_interest_rate
        rate = getattr(self, 'interest_rate', BankAccount.default_interest_rate)
        self.bal += self.bal * rate

# Create an instance with an initial balance
bank = BankAccount(1000)

# Apply interest with the default rate
bank.apply_interest()
print(bank.bal)  # Expected balance after 3% interest (1030.0)

# Override the instance interest rate
bank.interest_rate = 0.05  # Set to 5% for this instance
bank.apply_interest()
print(bank.bal)  # Expected balance after 5% interest

# Delete the instance attribute to revert to the class attribute
del bank.interest_rate
bank.apply_interest()
print(bank.bal)  # Expected balance with default 3% interest rate
