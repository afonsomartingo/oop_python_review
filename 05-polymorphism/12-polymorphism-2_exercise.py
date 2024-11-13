'''Problem Statement: Custom Length Calculator
Objective
Create a Python program that demonstrates polymorphism by implementing a custom function custom_len that mimics the behavior of Python's built-in len function. 
The custom_len function should return the length of an object if that object type supports it. The goal is to handle various data types like lists, dictionaries, and strings, 
each with different internal ways of storing "length."

Requirements
Define a function custom_len(obj):
The function should return the number of elements for lists and tuples.
For dictionaries, return the number of key-value pairs.
For strings, return the number of characters.
Class Requirement: Define a class CustomObject with a private length attribute _length and implement a __len__() method that returns this length.
Polymorphic Behavior: Your custom_len function should handle any object that has a __len__() method.'''

# Define the custom_len function to mimic Python's len function
def custom_len(obj):
    # Check if the object has a __len__() method
    if hasattr(obj, '__len__'):
        return obj.__len__()  # Use the object's own __len__ method
    else:
        return "Unsupported object type"  # Handle unsupported types

# Custom class with a private length attribute
class CustomObject:
    def __init__(self, length):
        self._length = length  # Private length attribute
    
    def __len__(self):
        return self._length  # Implement custom length based on attribute

# Sample objects for testing
sample_list = [1, 2, 3, 4]
sample_dict = {'a': 1, 'b': 2}
sample_string = "Hello"
custom_obj = CustomObject(10)

# Testing custom_len function with various types
print(custom_len(sample_list))    # Expected output: 4
print(custom_len(sample_dict))    # Expected output: 2
print(custom_len(sample_string))  # Expected output: 5
print(custom_len(custom_obj))     # Expected output: 10
print(custom_len(123))            # Expected output: "Unsupported object type"
