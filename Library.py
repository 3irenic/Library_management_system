class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print(f"List of books in {self.name, self.location} library:\n")
            for book in self.books:
                print(f"{book.title} by {book.author} - ISBN: {book.ISBN}, copies: {book.copies}")
