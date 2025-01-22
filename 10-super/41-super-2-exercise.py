'''
Exercise:

Create a Python program that demonstrates the use of abstract base classes (ABCs) and the super() function. Follow these steps:

Define an Abstract Base Class (Shape):

Create a class Shape with abc.ABCMeta as its metaclass.
Define an abstract method area that must be implemented by any subclass.
Define a concrete method set_dimensions that sets the dimensions of the shape.
Define a Derived Class (Rectangle):

Create a class Rectangle that inherits from Shape.
Implement the area method to calculate and return the area of the rectangle.
Override the set_dimensions method to ensure the dimensions are positive integers. If not, set them to 1.
Use the super() function to call the set_dimensions method from the Shape class within the Rectangle class's set_dimensions method.
Define Another Derived Class (Circle):

Create a class Circle that inherits from Shape.
Implement the area method to calculate and return the area of the circle.
Override the set_dimensions method to ensure the radius is a positive integer. If not, set it to 1.
Use the super() function to call the set_dimensions method from the Shape class within the Circle class's set_dimensions method.
Create Instances and Call Methods:

Create an instance of each class (Rectangle and Circle).
Set the dimensions for each instance.
Call the area method on each instance and print the result.'''

import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def area(self):
        pass
    
    def set_dimensions(self, *dimensions):
        self.dimensions = dimensions

class Rectangle(Shape):
    def area(self):
        length, height = self.dimensions
        return length * height
    
    def set_dimensions(self, length, height):
        if not isinstance(length, int) or not isinstance(height, int):
            length = 1
            height = 1
        super(Rectangle, self).set_dimensions(length, height)



class Circle(Shape):
    def area(self):
        radius, = self.dimensions
        return 3.14 * radius * radius
    
    def set_dimensions(self, radius):
        if not isinstance(radius, int):
            radius = 1
        super(Circle, self).set_dimensions(radius)


# Create instances
rectangle = Rectangle()
circle = Circle()

# Set dimensions
rectangle.set_dimensions(5, 10)
circle.set_dimensions(7)

# Print areas
print(rectangle.area())
print(circle.area())