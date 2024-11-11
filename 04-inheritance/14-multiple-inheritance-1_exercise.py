'''Problem Statement:
Create a Python program to simulate the behavior of an online store's User, Customer, and Admin roles using multiple inheritance.

Base Classes:

User:
Define a method login() which prints "User logged in".
Customer:
Define a method make_purchase() which prints "Purchase made by customer".
Admin:
Define a method delete_user() which prints "Admin deleted a user".
Derived Class:

SuperUser:
Inherit from Customer and Admin.
Implement a method view_dashboard() that prints "Viewing admin dashboard".
This class should have access to both make_purchase() from Customer and delete_user() from Admin.
Task:

Create an instance of SuperUser and call the methods login(), make_purchase(), delete_user(), and view_dashboard().
Demonstrate the MRO (Method Resolution Order) by printing the order in which the methods are searched and called when invoking the methods from the SuperUser instance.'''

class User:
    def login(self):
        print("User logged in")

class Customer(User):
    def make_purchase(self):
        print("Purchase made by customer")

class Admin(User):
    def delete_user(self):
        print("Admin deleted a user")

class Superuser(Customer, Admin):
    def view_dashboard(self):
        print("Viewing admin dashboard")


# Create an instance of Superuser and call the methods
super_instance = Superuser()
super_instance.login()         # Calls login from User
super_instance.make_purchase() # Calls make_purchase from Customer
super_instance.delete_user()   # Calls delete_user from Admin
super_instance.view_dashboard() # Calls view_dashboard from Superuser

# Display the MRO
print("\nMethod Resolution Order:")
print(Superuser.mro())
