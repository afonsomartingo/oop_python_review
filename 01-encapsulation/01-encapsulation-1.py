#!/usr/bin/env python

# encapsulation-1.py

# Encapsulation means to preserve data in classes using methods
# Here, we're setting the 'val' attribute through 'set_val()'.
# See the next example, `encapsulation-2.py` for more info

# In this example, we have two methods, `set_val` and `get_val`.
# The first one sets the `val` value while the second one
# prints/returns the value.


class MyClass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)
        return self.value


a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

a.get_val()
b.get_val()

# NOTE: If you run this code, it won't print anything to the screen.
# This is because, even if we're calling `a.get_val()` and `b.get_val()`,
# the `get_val()` function doesn't contain a `print()` function.
# If we want to get the output printed to screen, we should do any of
# the following:

# a) Either replace `return self.value` with `print(self.value)`
# or add a print statement **above** `return` as `print(self.value)`.

# b) Remove `return(self.value)` and replace it with `print(self.value)`
'''
class SpaceShuttle(object):
    def __init__(self, count):
        self.count = count + 1
    def speed_calcule(self):
        return self.count * 1000
    
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}") # 
        super().__setattr__(name, value)  # super() is used to call the parent class method, in this case, __setattr__(). __setattr__() is a built-in method in Python classes, which is called when an attribute assignment is made. It is used to set the attribute of an instance of a class.
    def __getattribute__(self, name):
        print(f"Getting {name}")
        return super().__getattribute__(name) # super() is used to call the parent class method, in this case, __getattribute__(). __getattribute__() is a built-in method in Python classes, which is called when an attribute is accessed. It is used to access the attribute of an instance of a class.

if __name__ == '__main__':
    
    count = 1
    S = SpaceShuttle(count)
    print(S.speed_calcule()) '''
