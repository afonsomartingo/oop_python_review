'''
Problem Statement: Understanding Encapsulation and Data Integrity

Objective: Build a class that properly encapsulates its attributes and restricts direct access to ensure data integrity.

Instructions:

Class Definition:

Create a class named SecureValue that encapsulates a single attribute value. This class should provide methods to set and get the value while maintaining encapsulation.
Encapsulation Requirements:

Implement a method called set_value to assign a value to value. This method should include validation to ensure that only positive integers can be assigned. If a negative integer or a non-integer value is provided, the method should raise a ValueError with an appropriate message.
Implement a method called get_value that returns the current value of value. It should also handle the case where value has not been set yet, returning a message like "Value not set" in such cases.
Testing Encapsulation:

Create instances of SecureValue and test both the set_value and get_value methods.
After setting values using the set_value method, ensure that you cannot directly modify the value attribute from outside the class (i.e., do not allow something like instance.value = 200).
Attempt to call set_value with invalid values and verify that the appropriate exceptions are raised.
Output Results:

Print the results of your get_value calls to demonstrate that the encapsulation is working correctly.
Bonus Challenge:

Implement a method called reset_value that sets value back to its initial state (e.g., None or some default value) while ensuring that the method can only be called internally, demonstrating the concept of private methods.'''

class SecureValue:
    def __init__(self):
        self.value = None

    def set_value(self, val):
        # Check if val is an integer and positive
        if not isinstance(val, int) or val <= 0:
            raise ValueError("Only positive integers can be assigned")
        self.value = val

    def get_value(self):
        # Return a message if the value is not set
        if self.value is None:
            return "Value not set"
        return self.value


# Testing the SecureValue class
if __name__ == "__main__":
    a = SecureValue()
    b = SecureValue()

    a.set_value(10)
    result = a.get_value()  # Correctly call the method
    print(f"Value of a: {result}")  # Prints the value of a

    # a.set_value = 200  # This line should not be allowed in encapsulation

    print(f"Value of b: {b.get_value()}")  # Should print "Value not set"
