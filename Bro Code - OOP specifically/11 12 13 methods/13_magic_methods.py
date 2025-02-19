"""
Magic Methods: Dunder methods (double underscore) 
__init__(): initialize an instance, __str__(): print(), __eq__(): ==, __lt__(): <, __gt__(): >,
__add__(): +, __contains__() : in, __getitem__() : access obj. attributes as keys e.g. obj['key'],

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
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, item):
        # __contains__() allows us to check if a specific value exists in a given sequence/collection
        # basically used with 'in' keyword (membership)
        # Tests if an object(item) exists in another object(self)
        return item in self.title or item in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key: '{key}' was not found"


book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and The Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Lion, The Witch and The Wardrobe", "C.S. Lewis", 100)

# print(book1)
# print(book2)
# print(book3)

# without the __eq__ dunder it was actually comparing the object references ie their memory address. So it was always False. But we customized
# print(book4 == book3)

# With the __gt__ we can now customize the behaviour we are seeing here
# print(book3 < book4)
# print(book3 > book4)

# adding 2 objects, after implementing __add__:
# print(book3 + book4)

# Search for a keyword using 'in' membership. Utilizes the __contains__()
print("Lion" in book3)

# We can also get attributes of an object as a key just like we do with dictionaries
print(book1['Auto'])
