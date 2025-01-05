'''
Exercise: Implementing a Shape Class Hierarchy

Objective: Create an abstract base class for shapes and implement concrete classes for specific shapes.

Instructions:
1. Create an Abstract Base Class:
    Define an abstract class named Shape using the abc module.
    This class should have the following abstract methods:
        area(): This method should return the area of the shape.
        perimeter(): This method should return the perimeter of the shape.

2. Implement Concrete Classes:
    Create two concrete classes that inherit from Shape:
        Rectangle: This class should have attributes for width and height. Implement the area() and perimeter() methods.
        Circle: This class should have an attribute for radius. Implement the area() and perimeter() methods.
3. Testing the Classes:
    Create instances of Rectangle and Circle.
    Print the area and perimeter for each shape.

4. Bonus Challenge:
    Add a method describe() in the Shape class that prints a description of the shape. Implement this method in both concrete classes to provide specific details about each shape.

Hints:
    Use the math module for calculations related to the circle (e.g., math.pi).
    Remember to use the @abc.abstractmethod decorator for the abstract methods in the Shape class.
'''

import abc
import math

class Shape(abc.ABC):

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print("This is a shape.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        print(f"This is a rectangle with width {self.width} and height {self.height}.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def describe(self):
        print(f"This is a circle with radius {self.radius}.")

# Testing the classes
rectangle = Rectangle(4, 5)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
rectangle.describe()

circle = Circle(3)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
circle.describe()