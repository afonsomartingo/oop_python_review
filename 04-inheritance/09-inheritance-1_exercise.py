'''Problem Statement: Class Inheritance and Method Access

Write a Python program with the following requirements:

Create a class named Person that has:

An attribute name, set during initialization.
A method greet() that prints a greeting message using the name attribute.
Create another class named Employee that:

Inherits from the Person class.
Has an additional attribute employee_id, set during initialization.
Has a method show_id() that prints the employee's ID.
Write a class named Manager that:

Inherits from the Employee class.
Has an additional attribute department, set during initialization.
Adds a method display_details() that prints the name, employee_id, and department of the Manager.
Create instances of each class (Person, Employee, and Manager):

For each instance, call all available methods and verify that each class can access methods and attributes from its parent classes.'''

class Person:
    def __init__(self, name):
        self.person_name = name
    
    def greet(self):
        print(f"Welcome, {self.person_name}!")


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)  # Call the parent class (Person) initializer
        self.employee_id = employee_id
    
    def show_id(self):
        print(f"Employee ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)  # Call the parent class (Employee) initializer
        self.department = department

    def display_details(self):
        print(f"Name: {self.person_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")


# Creating instances of each class and calling their methods
# Instance of Person
person = Person("André")
person.greet()

print("--------")

# Instance of Employee
employee = Employee("Maria", 101)
employee.greet()  # Inherited from Person
employee.show_id()

print("--------")

# Instance of Manager
manager = Manager("Carlos", 202, "Sales")
manager.greet()         # Inherited from Person
manager.show_id()       # Inherited from Employee
manager.display_details()  # Method from Manager
