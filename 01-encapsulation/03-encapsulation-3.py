#!/usr/bin/env python

# 03-encapsulation-3.py

# Here we look at another example, where we have three methods
# set_val(), get_val(), and increment_val().

# set_val() helps to set a value, get_val() prints the value,
# and increment_val() increments the set value by 1.

# We can still break encapsulation here by calling 'self.value'
# directly in an instance, which is **BAD**.

# set_val() forces us to input an integer, ie.. what the code wants
# to work properly. Here, it's possible to break the encapsulation by
# calling 'self.val` directly, which will cause unexpected results later.
# In this example, the code is written to enforce an intger as input, if we
# don't break encapsulation and go through the gateway 'set_val()'

#


class MyInteger(object):
    def set_val(self, val): # <== This method forces us to input an integer
        try:
            val = int(val)
        except ValueError: # <== This is a good practice because it will catch any errors that might occur for example if a string is passed
            return
        self.val = val

    def get_val(self): # <== This method prints the value
        print(self.val)

    def increment_val(self): # <== This method increments the value by 1
        self.val = self.val + 1
        print(self.val)


a = MyInteger()
a.set_val(10) # <== Setting the value to 10
a.get_val() # <== Printing the value
a.increment_val() # <== Incrementing the value by 1
print("\n")

# Trying to break encapsulation in a new instance with an int
c = MyInteger()
c.val = 15 # <== Breaking encapsulation, works fine
c.get_val() # <== Prints the val set by breaking encap
c.increment_val()
print("\n")

# Trying to break encapsulation in a new instance with a str
b = MyInteger()
b.val = "MyString"  # <== Breaking encapsulation, works fine
b.get_val()  # <== Prints the val set by breaking encap
b.increment_val()  # This will fail, since str + int wont work
print("\n")
