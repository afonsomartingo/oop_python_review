'''Problem Statement: School Library System
You are building a simplified school library system with a class named Book. Each book has a class attribute and an instance attribute.

Requirements
Define a Book class that:

Has a class attribute library_name set to "Downtown High School Library" (all books belong to the same library).
Has an instance attribute book_title, which stores the title of the book. Set this attribute by defining an __init__ method that takes book_title as a parameter.
Write a method display_info in the Book class that:

Prints the library name using the class attribute library_name.
Prints the title of the book using the instance attribute book_title.
Create two instances of the Book class with different book titles (e.g., "To Kill a Mockingbird" and "1984") and call display_info on each instance.

Expected Output
The output should display the library name and the book title for each instance. The library name should be the same for both instances, while the book titles should be different.'''

class Book:
    library_name = "Downtown High School Library"  # Class attribute

    def __init__(self, book_title):
        self.book_tit = book_title  # Instance attribute

    def display_info(self):
        print(f"Library: {Book.library_name}")  # Accessing the class attribute
        print(f"Title: {self.book_tit}\n")  # Accessing the instance attribute

if __name__ == "__main__":
    # Creating instances with book titles
    book1 = Book("To Kill a Mockingbird")
    book2 = Book("1984")

    # Displaying information for each book
    book1.display_info()
    book2.display_info()

