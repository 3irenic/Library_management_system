from datetime import datetime, timedelta

class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.issued_date = datetime.now()
        self.return_date = None

    def return_book(self):
        self.return_date = datetime.now()

    def get_due_date(self):
        return self.issued_date + timedelta(days=14)

    def is_overdue(self):
        due_date = self.get_due_date()
        return datetime.now() > due_date

    def __str__(self):
        due_date = self.get_due_date().strftime("%d/%m/%Y")
        if self.return_date:
            return f"{self.book.title} by {self.book.author} - borrowed by {self.member.name} - Due: {due_date}, Returned: {self.return_date.strftime('%d/%m/%Y')}"
        else:
            return f"{self.book.title} by {self.book.author} - borrowed by {self.member.name} - Due: {due_date}"

    def __repr__(self):
        return f"Loan({repr(self.book)}, {repr(self.member)})"
