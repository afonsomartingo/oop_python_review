"""Exercise: Extend the InstanceCounter Class

1. Add a New Method: Create a method called reset_count in the InstanceCounter class that resets the class variable count back to 0.

Modify the Constructor: Update the __init__ method to accept an optional parameter reset (default value should be False). If reset is True, call the reset_count method to reset the count whenever a new instance is created.

Create a New Instance: After creating instances a, b, and c, create a new instance d with the value 20 and reset set to True.

Print the Values and Count: After creating all instances, print the value of each instance and the total count of instances created.

Expected Output
You should see the values of the instances and the count reflecting the reset after creating instance d.
"""
class InstanceCounter(object):
    count = 0

    def __init__(self, val, reset=False):
        self.val = val
        InstanceCounter.count += 1
        if reset:
            self.reset_count()

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

    def reset_count(self):
        InstanceCounter.count = 0

# Create instances a, b, c, and d
a = InstanceCounter(80)
print(a.get_val())
b = InstanceCounter(40)
print(b.get_val())
c = InstanceCounter(20)
print(c.get_val())
d = InstanceCounter(20, reset=True)
print(d.get_val())

# Print total count of instances created
print("Total instances created:", InstanceCounter.count)
