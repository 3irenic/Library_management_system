class Book:
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} - ISBN: {self.ISBN}, copies: {self.copies}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.ISBN}', {self.copies})"
