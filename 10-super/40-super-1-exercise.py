'''
Exercise:

Create a Python program that demonstrates the use of the super() function in a multi-level inheritance scenario. Follow these steps:

Define a Base Class (Animal):

Create a class Animal with a method sound that prints "Animals make sounds".
Define a Derived Class (Mammal):

Create a class Mammal that inherits from Animal.
Override the sound method to print "Mammals make specific sounds".
Use the super() function to call the sound method from the Animal class within the Mammal class's sound method.
Define Another Derived Class (Dog):

Create a class Dog that inherits from Mammal.
Override the sound method to print "Dogs bark".
Use the super() function to call the sound method from the Mammal class within the Dog class's sound method.
Create Instances and Call Methods:

Create an instance of each class (Animal, Mammal, and Dog).
Call the sound method on each instance and observe the output.'''

class Animal:
    def sound(self):
        print("Animals make sounds")

class Mammal(Animal):
    def sound(self):
        print("Mammals make specific sounds")
        super(Mammal, self).sound()

class Dog(Mammal):
    def sound(self):
        print("Dogs bark")
        super(Dog,self).sound()


animal = Animal()
mammal = Mammal()
dog = Dog()

animal.sound()
mammal.sound()
dog.sound()
