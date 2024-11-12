'''Problem: Zoo Animal Interaction
Problem Statement:

You are tasked with creating a program that simulates the interaction between different animals in a zoo. You will have to implement a base class Animal and then derive two subclasses Lion and Elephant. Each subclass should have a sound method, but they will return different outputs based on the animal. Additionally, the Animal class will have a method feed which takes a food parameter and prints a message saying that the animal eats the food.

The program should then loop through a list of different animals and call their sound and feed methods, showing polymorphism in action.

Requirements:

Define a class Animal with the following attributes and methods:

__init__(self, name) - Initializes the animal's name.
sound(self) - A method that prints a generic sound for any animal.
feed(self, food) - A method that prints a message that the animal eats the food provided.
Define a class Lion that inherits from Animal and overrides the sound method to print "Roar!" and the feed method to print that the lion eats meat.

Define a class Elephant that inherits from Animal and overrides the sound method to print "Trumpet!" and the feed method to print that the elephant eats grass.

Create a list of animals (Lion and Elephant objects). Loop through the list and call the sound and feed methods for each animal, demonstrating polymorphism.
'''

class Animal():
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("{0} makes a generic sound.".format(self.name))
    def feed(self, food):
        print("{0} eats {1}.".format(self.name, food))

class Lion(Animal):
    def sound(self):
        print("{0} roars!".format(self.name))
    
    def feed(self, food):
        print("{0} eats meat.".format(self.name))

class Elephant(Animal):
    def sound(self):
        print("{0} trumpets!".format(self.name))

    def feed(self, food):
        print("{0} eats grass.".format(self.name))

# Create a list of different animals
animals = [Lion("Simba"), Elephant("Dumbo"), Lion("Mufasa"), Elephant("Jumbo")]

for animal in animals:
    animal.sound()
    animal.feed("food")