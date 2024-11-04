'''Problem Statement: Custom Number Class
Create a class called CustomNumber that encapsulates a numerical value and includes methods for arithmetic operations. The class should perform the following tasks:

Initialization: In the constructor (__init__ method), check if the provided value is an integer. If it is not, default the value to 0.

Increment Method: Define an increment method that increases the stored value by 1 and returns the new value.

Decrement Method: Define a decrement method that decreases the stored value by 1 and returns the new value.

Add Method: Define an add method that takes another CustomNumber instance as an argument, adds its value to the current instance, and returns the result.

Subtract Method: Define a subtract method that takes another CustomNumber instance as an argument, subtracts its value from the current instance, and returns the result.

String Representation: Override the __str__ method to return the current value as a string.'''

class CustomNumber:
    def __init__(self, value):
        if isinstance(value, int): 
            self.val = value
        else:
            self.val = 0

    def increment(self):
        self.val += 1
        return self.val  # Return the new value

    def decrement(self):
        self.val -= 1
        return self.val  # Return the new value
    
    def add(self, other):
        if isinstance(other, CustomNumber): # Check if 'other' is an instance of CustomNumber
            return self.val + other.val
        else:
            raise ValueError("Argument must be an instance of CustomNumber")
    
    def subtract(self, other):
        if isinstance(other, CustomNumber):
            return self.val - other.val
        else:
            raise ValueError("Arg-ument must be an instance of CustomNumber")
    
    def __str__(self): 
        return str(self.val)  # String representation of the value

# Example usage
num1 = CustomNumber(5)
print(num1.increment())  # Should print 6
print(num1.decrement())  # Should print 5

num2 = CustomNumber("not a number")  # Should default to 0
print(num2.increment())  # Should print 1

result = num1.add(num2)
print(result)  # Should print 6

result = num1.subtract(num2)
print(result)  # Should print 5
