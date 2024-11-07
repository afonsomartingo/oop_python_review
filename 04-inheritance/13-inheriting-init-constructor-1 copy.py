'''Problem Statement: "Inheriting and Extending Animal Behaviors"
Problem

You are given a base class Animal with a constructor that takes one argument, name, and stores it as an instance attribute. Create the following subclasses that inherit from Animal:

Dog:

Inherits the Animal class.
Add an attribute breed to store the dog’s breed.
Modify the constructor to take an additional argument breed.
Implement a method fetch() that takes one argument thing and prints: "[name] the [breed] goes after the [thing]".
Cat:

Inherits the Animal class.
Add an attribute lives_left which defaults to 9 if not specified.
Implement a method meow() that prints: "[name] says 'Meow!'".
Implement a method lose_life() which decreases lives_left by 1 and prints the number of lives left. If lives_left is already 0, print: "[name] has no lives left.".
Bird:

Inherits the Animal class.
Add an attribute can_fly that is True by default but can be set to False when creating the instance.
Implement a method fly() that prints: "[name] flies in the sky." if can_fly is True. Otherwise, it should print: "[name] can't fly.".
'''

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def fetch(self, thing):
        print(f"{self.name} the {self.breed} goes after the {thing}.")

class Cat(Animal):
    def __init__(self, name, lives_left=9):
        super().__init__(name)
        self.lives_left = lives_left
    
    def meow(self):
        print(f"{self.name} says 'Meow!'")

    def lose_life(self):
        self.lives_left -= 1
        if self.lives_left == 0:
            print(f"{self.name} has no lives left.")
        else:
            print(f"{self.name} has {self.lives_left} lives left.")

class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly
    
    def fly(self):
        if self.can_fly:
            print(f"{self.name} flies in the sky.")
        else:
            print(f"{self.name} can't fly.")

# Testing
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")
bird = Bird("Polly", can_fly=False)

dog.fetch("ball")
cat.meow()
cat.lose_life()
bird.fly()

