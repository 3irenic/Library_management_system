from Library import Library
from Book import Book
from Member import Member 
from Loan import Loan


class main():
    # create a Library instance
    library = Library("Central Library", "Kokomeng")
    

    # add books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 5)
    library.add_book(book1)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0446310789", 3)
    library.add_book(book2)
    book3 = Book("1984", "George Orwell", "978-0451524935", 7)
    library.add_book(book3)

    # display all books in the library
    library.display_books()

    # create a Member instance
    member1 = Member("Lesedi Sebekedi", "M123")

    # print the member object
    print("The members are: ",member1)                # John Doe - Membership No: M123

    # create a Loan instance
    loan1 = Loan(book1, member1)

    # print the loan object
    print(loan1)                  # The Great Gatsby by F. Scott Fitzgerald - borrowed by John Doe - Due

main()