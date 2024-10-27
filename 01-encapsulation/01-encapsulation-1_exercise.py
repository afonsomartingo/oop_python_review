'''Exercise 1: Encapsulation 

Exercise: Enhancing MyClass with Data Validation

Objective: Modify the MyClass class to include data validation when setting the value, and add an additional method to retrieve the value as a string.

Instructions:
Data Validation:

Update the set_val method to check if the provided value is an integer. If it is not, raise a ValueError with a message saying "Value must be an integer." If the value is valid, set the value attribute.
String Representation:

Implement a new method called get_val_as_string that returns the value attribute as a string. This method should also include a check to ensure that the value is set before trying to return it. If value is not set, it should return "Value not set."
Testing:

Create instances of MyClass and test both the set_val and the new get_val_as_string methods. Ensure that your tests include cases where an invalid value is provided.
Print Results:

Use print statements to display the results of the methods after setting values. Make sure to handle exceptions raised by invalid inputs gracefully.
'''

class MyClass(object):
    def __init__(self):
        self.value = None  # Initialize value to None

    def set_val(self, val):
        if not isinstance(val, int):
            raise ValueError("Value must be an integer.")
        self.value = val

    def get_val(self):
        if self.value is None:
            print("Value not set")
            return None
        print(self.value)
        return self.value
    
    def get_val_as_string(self):
        if self.value is None:
            return "Value not set"
        return str(self.value)

# Testing the MyClass functionality
if __name__ == "__main__":
    a = MyClass()
    b = MyClass()

    # Test valid setting of values
    try:
        a.set_val(10)
        b.set_val(100)
    except ValueError as e:
        print(e)

    # Print values using the methods
    print(a.get_val())  # Should print 10
    print(b.get_val())  # Should print 100

    print(a.get_val_as_string())  # Should print "10"
    print(b.get_val_as_string())  # Should print "100"
