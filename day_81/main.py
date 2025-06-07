class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"


book1 = Book("1984", "George Orwell", 1949)

# __str__ is used when printing the object
print(book1)  # Output: 1984 by George Orwell (1949)

# __repr__ is used for developers and debugging
print(repr(book1))  # Output: Book('1984', 'George Orwell', 1949)
