'''Problem Statement: Integer Manipulator with Encapsulation

Objective
Implement a class IntegerManipulator that encapsulates an integer value and provides a controlled interface to manipulate this value. The class should ensure that only valid 
integer operations are allowed and should prevent any direct access to the integer attribute, enforcing encapsulation.

Requirements
Methods:

set_value(val): Accepts an integer value val and sets it as the internal integer value. This method should only accept integers. If the input is not an integer, it should 
raise a ValueError with the message "Value must be an integer."

get_value(): Returns the current integer value.
increment(): Increases the stored integer by 1.
decrement(): Decreases the stored integer by 1.
Encapsulation:

The internal value should not be directly accessible from outside the class. Attempting to access or modify the value directly should lead to an error or simply not be possible.
Usage:

Demonstrate the correct usage of the IntegerManipulator class.
Show what happens when trying to set a non-integer value.
Demonstrate an attempt to access the internal value directly (this should fail or be prevented).
Constraints
The class should only work with integers and should not allow any other types.
Aim for clean and organized code with good exception handling.'''

class IntegerManipulator:
    def __init__(self):
        self.__val = 0  # Make value private to reinforce encapsulation

    def set_value(self, value):
        if isinstance(value, int):  # Check if the value is an integer
            self.__val = value
        else:
            raise ValueError("Value must be an integer.")  # Raise an error for non-integer input

    def get_value(self):
        return self.__val  # Return the private value

    def increment(self):
        self.__val += 1  # Increase the private value by 1
        
    def decrement(self):
        self.__val -= 1  # Decrease the private value by 1

# Example usage
manipulator = IntegerManipulator()
manipulator.set_value(10)
print(manipulator.get_value())   # Output: 10
manipulator.increment()
print(manipulator.get_value())   # Output: 11
manipulator.decrement()
print(manipulator.get_value())   # Output: 10

try:
    manipulator.set_value("abc")  # Raises ValueError
except ValueError as e:
    print(e)   # Output: "Value must be an integer."
