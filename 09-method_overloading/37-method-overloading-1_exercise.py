'''Exercise: Vehicle Class Hierarchy

Objective: Create an abstract base class for vehicles and implement concrete classes for specific types of vehicles.

Instructions:

1. Create an Abstract Base Class:
    Define an abstract class named Vehicle using the abc module.
    This class should have the following abstract methods:
        start_engine(): This method should return a string indicating that the engine has started.
        stop_engine(): This method should return a string indicating that the engine has stopped.
        drive(): This method should return a string indicating that the vehicle is being driven.
        describe(): This method should return a string describing the vehicle.

2. Implement Concrete Classes:
    Create two concrete classes that inherit from Vehicle:
        Car: This class should have an attribute for make and model. Implement the abstract methods and include a method describe() that prints the make and model of the car.
        Motorcycle: This class should have an attribute for brand. Implement the abstract methods and include a method describe() that prints the brand of the motorcycle.
    Testing the Classes:
        Create instances of Car and Motorcycle.
        Call the start_engine(), drive(), and stop_engine() methods for each vehicle and print the results.
        Call the describe() method for each vehicle.

Bonus Challenge:
    Add a method fuel_type() in the Vehicle class that returns the type of fuel used by the vehicle. Implement this method in both concrete classes to provide specific details about the fuel type.

Hints:
    Use the @abc.abstractmethod decorator for the abstract methods in the Vehicle class.
    Remember to use the super() function to call methods from the parent class if needed.
'''

import abc

class Vehicle(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def start_engine(self):
        pass
    
    @abc.abstractmethod
    def stop_engine(self):
        pass
    
    @abc.abstractmethod
    def drive(self):
        pass

    @abc.abstractmethod
    def describe(self):
        pass
    

class Car(Vehicle):
    
    def __init__(self, model, make):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started"

    def stop_engine(self):
        return "Engine stopped"

    def drive(self):
        return "Vehicle is being driven"

    def describe(self):
        return f"This is a {self.make} {self.model}."


# Testing the Car class
if __name__ == "__main__":
    my_car = Car("Corolla", "Toyota")
    print(my_car.start_engine())
    print(my_car.drive())
    print(my_car.stop_engine())
    print(my_car.describe())