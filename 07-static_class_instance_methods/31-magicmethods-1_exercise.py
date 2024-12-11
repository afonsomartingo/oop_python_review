"""Exercise: Extend the PrintList Class

1. Add a New Method: Implement a method called __len__() in the PrintList class that returns the length of the list stored in mylist.

2.Implement __getitem__(): Add a method called __getitem__(index) that allows you to access elements of mylist using indexing (e.g., printlist[0] should return the first element).

3. Implement __add__(): Create a method called __add__(other) that allows you to concatenate another list to mylist. For example, if other is a list, printlist + other should return a new PrintList object containing the combined lists.

4. Create Instances and Test: After implementing the above methods, create an instance of PrintList with a list of your choice. Test the __len__(), __getitem__(), and __add__() methods and print the results.
"""

class PrintList(object):
    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)

    def __len__(self):
        return len(self.mylist)

    def __getitem__(self, index):
        return self.mylist[index]

    def __add__(self, other):
        if isinstance(other, list):  # Check if other is a list
            return PrintList(self.mylist + other)  # Return a new PrintList with the combined lists
        return NotImplemented  # Return NotImplemented for unsupported types


# Create an instance of PrintList
printlist = PrintList(["a", "b", "c"])

# Test __len__()
print("Length of printlist:", len(printlist))

# Test __getitem__()
print("First item:", printlist[0])

# Test __add__()
new_list = printlist + ["d", "e", "f"]
print("New list after addition:", new_list)