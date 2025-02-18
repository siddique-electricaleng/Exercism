"""
Magic Methods: Dunder methods (double underscore) __init__, __str__, __eq__, __gt__

__eq__ : compare if 2 objects are equal by comparing their attributes or whatever.      Return value depends on user
__gt__ : compare if an attribute between 2 objects are greater than which.              Return value depends on user

These methods are automatically called by many of Python's built-in operations.
They allow developers to define or customize the behavior of objects.
"""


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages


book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and The Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Lion, The Witch and The Wardrobe", "C.S. Lewis", 100)

print(book1)
print(book2)
print(book3)

# without the __eq__ dunder it was actually comparing the object references ie their memory address. So it was always False. But we customized
print(book4 == book3)
# With the __gt__ we can now customize the behaviour we are seeing here
print(book3 < book4)
print(book3 > book4)
# adding 2 objects, after implementing __add__:
print(book3 + book4)
