'''Problem: Object Counter Class
Description:

You are tasked with creating a class called ObjectCounter that helps keep track of the number of instances created from the class. Each instance should have a unique ID assigned to it, which is an incrementing number starting from 1. Additionally, each instance will have an info attribute containing a string, which can be set at the time of instantiation.

The class should have the following methods:

__init__(self, info):

Initializes the instance with a unique ID and assigns the info attribute.
Updates the class attribute count each time a new instance is created.
get_instance_info(self):

Prints the instance's unique ID and its info attribute.
get_total_instances() (class method):

Prints the total number of instances created so far.'''

class ObjectCounter:
    count = 0

    def __init__(self, info):
        ObjectCounter.count += 1
        self.ID = ObjectCounter.count
        self.info = info

    def get_instance_info(self):
        print(f"ID number: {self.ID}")
        print(f"Info: {self.info}")

    @classmethod
    def get_total_instances(cls):
        print(f"Total number of instances created so far: {cls.count}")


a = ObjectCounter("First instance")
b = ObjectCounter("Second instance")
c = ObjectCounter("Third instance")

a.get_instance_info()
b.get_instance_info()
c.get_instance_info()
ObjectCounter.get_total_instances()
