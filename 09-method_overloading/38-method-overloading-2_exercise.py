'''Exercise Description

Create a new class called GetSetInteger that inherits from GetSetParent and implements special handling for integer values. This will help you practice method overloading and working with abstract base classes.

Requirements:

1. Create a class GetSetInteger that inherits from GetSetParent
2. Override the set_val method to:
    Accept only integer values
    Raise a TypeError if the input is not an integer
    Store both the current value and its square
3. Override the get_val method to:
    Return a tuple of (value, square_of_value)
4. Implement the required showdoc method to:
    Print information about the class's special integer handling'''

class GetSetInteger(GetSetParent):
    def __init__(self, value=None):
        self._value = None
        self._square = None
        if value is not None:
            self.set_val(value)
    
    def set_val(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        self._value = value
        self._square = value ** 2
    
    def get_val(self):
        return (self._value, self._square)
    
    def showdoc(self):
        print("GetSetInteger class handles integer values only.")
        print("It stores both the value and its square.")
        print("get_val() returns a tuple of (value, square_of_value)")
    
