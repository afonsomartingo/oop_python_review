'''Problem Statement: "Zoo Simulation"
Objective: Create a small program that simulates animals in a zoo, focusing on inheritance and method access between classes.

Base Class - Animal:

Define a base class Animal with the following attributes and methods:
An __init__ method that accepts the name and age of the animal and assigns them to instance attributes.
A method eat that takes a food parameter and prints a message indicating the animal is eating that food.
A method sleep that prints a message indicating the animal is sleeping.
Subclass - Lion:

Create a subclass Lion that inherits from Animal.
Add an additional method roar, which prints a message indicating the lion is roaring.
Subclass - Elephant:

Create another subclass Elephant that inherits from Animal.
Add an additional method spray_water, which prints a message indicating the elephant is spraying water.
Instance Creation:

Create instances of both Lion and Elephant, each with unique names and ages.
Call the eat and sleep methods on both instances to demonstrate inheritance.
Call the roar method on the Lion instance and the spray_water method on the Elephant instance.
Access Control:

Attempt to call roar on the Elephant instance and spray_water on the Lion instance.
Observe and explain why these calls fail.'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self, food):
        print(f"{self.name} is eating {food}")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def roar(self):
        print(f"{self.name} is roaring!")   

class Elephant(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def spray_water(self):
        print(f"{self.name} is spraying water!") 

# Creating instances
lion_instance = Lion("Simba", 12)
elephant_instance = Elephant("Ramon", 7)

# Calling methods
lion_instance.eat("meat")
elephant_instance.sleep()

lion_instance.roar()
elephant_instance.spray_water()


# These calls will result in errors
# Uncommenting the lines below will raise AttributeError
# elephant_instance.roar()
# lion_instance.spray_water()