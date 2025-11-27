"""
Complex Library Management System
Demonstrates: Classes, Objects, Composition, Aggregation, Collections, Date handling
"""

from datetime import datetime, timedelta
from enum import Enum


class BookGenre(Enum):
    """Enum for book genres"""
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE = "Science"
    HISTORY = "History"
    BIOGRAPHY = "Biography"
    MYSTERY = "Mystery"
    FANTASY = "Fantasy"
    ROMANCE = "Romance"


class Book:
    """Represents a book in the library"""

    def __init__(self, isbn, title, author, genre, publication_year, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.borrowed_by = []  # List of member IDs who borrowed this book

    def is_available(self):
        return self.available_copies > 0

    def borrow(self, member_id):
        if self.is_available():
            self.available_copies -= 1
            self.borrowed_by.append(member_id)
            return True
        return False

    def return_book(self, member_id):
        if member_id in self.borrowed_by:
            self.available_copies += 1
            self.borrowed_by.remove(member_id)
            return True
        return False

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year}) - Available: {self.available_copies}/{self.total_copies}"


class Member:
    """Represents a library member"""

    member_id_counter = 1000

    def __init__(self, name, email, phone, membership_type="Regular"):
        self.member_id = Member.member_id_counter
        Member.member_id_counter += 1
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type  # Regular, Premium, Student
        self.registration_date = datetime.now()
        self.borrowed_books = {}  # {isbn: borrow_date}
        self.borrowing_history = []
        self.fines = 0.0

        # Different membership types have different limits
        self.max_books = {"Regular": 3, "Premium": 10, "Student": 5}[membership_type]
        self.borrow_duration = {"Regular": 14, "Premium": 30, "Student": 21}[membership_type]

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books and self.fines == 0

    def borrow_book(self, book):
        if not self.can_borrow():
            return False, "Cannot borrow: Limit reached or fines pending"

        if book.borrow(self.member_id):
            self.borrowed_books[book.isbn] = datetime.now()
            return True, f"Successfully borrowed '{book.title}'"
        return False, "Book not available"

    def return_book(self, book):
        if book.isbn not in self.borrowed_books:
            return False, "You haven't borrowed this book", 0

        borrow_date = self.borrowed_books[book.isbn]
        days_borrowed = (datetime.now() - borrow_date).days

        # Calculate fine if overdue
        fine = 0
        if days_borrowed > self.borrow_duration:
            overdue_days = days_borrowed - self.borrow_duration
            fine = overdue_days * 0.50  # $0.50 per day
            self.fines += fine

        book.return_book(self.member_id)
        del self.borrowed_books[book.isbn]

        # Add to history
        self.borrowing_history.append({
            "book": book.title,
            "borrow_date": borrow_date,
            "return_date": datetime.now(),
            "days": days_borrowed,
            "fine": fine
        })

        return True, f"Returned '{book.title}' after {days_borrowed} days", fine

    def pay_fine(self, amount):
        if amount >= self.fines:
            paid = self.fines
            self.fines = 0
            return True, f"Paid ${paid:.2f}. No pending fines."
        else:
            self.fines -= amount
            return True, f"Paid ${amount:.2f}. Remaining fine: ${self.fines:.2f}"

    def get_membership_duration(self):
        duration = datetime.now() - self.registration_date
        return duration.days

    def __str__(self):
        return (f"Member #{self.member_id}: {self.name} ({self.membership_type})\n"
                f"  Email: {self.email} | Phone: {self.phone}\n"
                f"  Books Borrowed: {len(self.borrowed_books)}/{self.max_books}\n"
                f"  Pending Fines: ${self.fines:.2f}\n"
                f"  Member for: {self.get_membership_duration()} days")


class Library:
    """Main library system that manages books and members"""

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = {}  # {isbn: Book}
        self.members = {}  # {member_id: Member}
        self.transaction_log = []

    def add_book(self, book):
        if book.isbn in self.books:
            # If book exists, increase copies
            self.books[book.isbn].total_copies += book.total_copies
            self.books[book.isbn].available_copies += book.total_copies
            return f"Added {book.total_copies} more copies of '{book.title}'"
        else:
            self.books[book.isbn] = book
            return f"New book added: '{book.title}'"

    def register_member(self, member):
        self.members[member.member_id] = member
        self.log_transaction(f"New member registered: {member.name} (ID: {member.member_id})")
        return member.member_id

    def find_book_by_title(self, title):
        results = []
        for book in self.books.values():
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def find_books_by_author(self, author):
        results = []
        for book in self.books.values():
            if author.lower() in book.author.lower():
                results.append(book)
        return results

    def find_books_by_genre(self, genre):
        results = []
        for book in self.books.values():
            if book.genre == genre:
                results.append(book)
        return results

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found"
        if isbn not in self.books:
            return False, "Book not found"

        member = self.members[member_id]
        book = self.books[isbn]

        success, message = member.borrow_book(book)
        if success:
            self.log_transaction(f"Member {member.name} borrowed '{book.title}'")
        return success, message

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found", 0
        if isbn not in self.books:
            return False, "Book not found", 0

        member = self.members[member_id]
        book = self.books[isbn]

        success, message, fine = member.return_book(book)
        if success:
            self.log_transaction(f"Member {member.name} returned '{book.title}'. Fine: ${fine:.2f}")
        return success, message, fine

    def log_transaction(self, message):
        self.transaction_log.append({
            "timestamp": datetime.now(),
            "message": message
        })

    def get_library_stats(self):
        total_books = sum(book.total_copies for book in self.books.values())
        available_books = sum(book.available_copies for book in self.books.values())
        borrowed_books = total_books - available_books
        total_fines = sum(member.fines for member in self.members.values())

        return {
            "total_books": total_books,
            "unique_titles": len(self.books),
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_members": len(self.members),
            "total_fines_pending": total_fines
        }

    def display_stats(self):
        stats = self.get_library_stats()
        print(f"\n{'='*60}")
        print(f"LIBRARY STATISTICS - {self.name}")
        print(f"{'='*60}")
        print(f"Total Books: {stats['total_books']} ({stats['unique_titles']} unique titles)")
        print(f"Available: {stats['available_books']} | Borrowed: {stats['borrowed_books']}")
        print(f"Total Members: {stats['total_members']}")
        print(f"Total Fines Pending: ${stats['total_fines_pending']:.2f}")
        print(f"{'='*60}\n")

    def display_all_books(self):
        print(f"\n--- All Books in {self.name} ---")
        for book in self.books.values():
            print(f"  [{book.isbn}] {book}")

    def display_all_members(self):
        print(f"\n--- All Members of {self.name} ---")
        for member in self.members.values():
            print(f"\n{member}")

    def __str__(self):
        return f"{self.name} Library\nLocation: {self.address}"


# ============================================
# DEMONSTRATION WITH COMPLEX OBJECTS
# ============================================

if __name__ == "__main__":
    print("="*70)
    print("COMPLEX LIBRARY MANAGEMENT SYSTEM")
    print("="*70)

    # Create Library
    library = Library("City Central Library", "123 Main Street, Downtown")
    print(f"\n{library}\n")

    # Create complex book objects
    book1 = Book("978-0-7432-7356-5", "1984", "George Orwell",
                 BookGenre.FICTION, 1949, 5)
    book2 = Book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee",
                 BookGenre.FICTION, 1960, 3)
    book3 = Book("978-0-553-29698-2", "A Brief History of Time", "Stephen Hawking",
                 BookGenre.SCIENCE, 1988, 4)
    book4 = Book("978-0-345-39180-3", "Dune", "Frank Herbert",
                 BookGenre.FANTASY, 1965, 2)
    book5 = Book("978-0-14-017739-8", "1984", "George Orwell",
                 BookGenre.FICTION, 1949, 3)  # Duplicate for testing

    # Add books to library
    print("\n--- Adding Books to Library ---")
    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))
    print(library.add_book(book4))
    print(library.add_book(book5))  # Will increase copies of existing book

    # Create complex member objects with different membership types
    member1 = Member("Alice Johnson", "alice@email.com", "555-0101", "Premium")
    member2 = Member("Bob Smith", "bob@email.com", "555-0102", "Regular")
    member3 = Member("Charlie Davis", "charlie@email.com", "555-0103", "Student")
    member4 = Member("Diana Prince", "diana@email.com", "555-0104", "Regular")

    # Register members
    print("\n--- Registering Members ---")
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)
    library.register_member(member4)
    print(f"Registered {len(library.members)} members")

    # Display initial state
    library.display_all_books()
    library.display_stats()

    # Simulate borrowing operations
    print("\n" + "="*70)
    print("BORROWING OPERATIONS")
    print("="*70)

    # Alice borrows multiple books (Premium member can borrow up to 10)
    print(f"\n--- {member1.name} (Premium Member) Borrowing ---")
    success, msg = library.borrow_book(member1.member_id, book1.isbn)
    print(msg)
    success, msg = library.borrow_book(member1.member_id, book3.isbn)
    print(msg)
    success, msg = library.borrow_book(member1.member_id, book4.isbn)
    print(msg)

    # Bob borrows books (Regular member can borrow up to 3)
    print(f"\n--- {member2.name} (Regular Member) Borrowing ---")
    success, msg = library.borrow_book(member2.member_id, book2.isbn)
    print(msg)
    success, msg = library.borrow_book(member2.member_id, book1.isbn)
    print(msg)

    # Charlie borrows books (Student member can borrow up to 5)
    print(f"\n--- {member3.name} (Student Member) Borrowing ---")
    success, msg = library.borrow_book(member3.member_id, book3.isbn)
    print(msg)

    # Display updated stats
    library.display_stats()

    # Search functionality
    print("\n" + "="*70)
    print("SEARCH OPERATIONS")
    print("="*70)

    print("\n--- Searching for '1984' ---")
    results = library.find_book_by_title("1984")
    for book in results:
        print(f"  Found: {book}")

    print("\n--- Searching for author 'Orwell' ---")
    results = library.find_books_by_author("Orwell")
    for book in results:
        print(f"  Found: {book}")

    print("\n--- All Fiction books ---")
    results = library.find_books_by_genre(BookGenre.FICTION)
    for book in results:
        print(f"  {book}")

    # Simulate returns with overdue fines
    print("\n" + "="*70)
    print("RETURN OPERATIONS")
    print("="*70)

    # Simulate overdue by manipulating borrow date
    print(f"\n--- Simulating overdue return for {member2.name} ---")
    member2.borrowed_books[book2.isbn] = datetime.now() - timedelta(days=20)  # 20 days ago
    success, msg, fine = library.return_book(member2.member_id, book2.isbn)
    print(msg)
    if fine > 0:
        print(f"  OVERDUE FINE: ${fine:.2f}")

    print(f"\n--- {member1.name} returning books (on time) ---")
    success, msg, fine = library.return_book(member1.member_id, book1.isbn)
    print(msg)

    # Display member information
    print("\n" + "="*70)
    print("MEMBER INFORMATION")
    print("="*70)
    library.display_all_members()

    # Pay fines
    print("\n" + "="*70)
    print("FINE PAYMENT")
    print("="*70)
    print(f"\n{member2.name} has ${member2.fines:.2f} in fines")
    success, msg = member2.pay_fine(5.0)
    print(msg)

    # Show borrowing history
    print("\n" + "="*70)
    print("BORROWING HISTORY")
    print("="*70)
    print(f"\n--- {member2.name}'s History ---")
    for record in member2.borrowing_history:
        print(f"  Book: {record['book']}")
        print(f"  Borrowed: {record['borrow_date'].strftime('%Y-%m-%d')}")
        print(f"  Returned: {record['return_date'].strftime('%Y-%m-%d')}")
        print(f"  Duration: {record['days']} days")
        print(f"  Fine: ${record['fine']:.2f}\n")

    # Final stats
    library.display_stats()

    # Transaction log
    print("\n" + "="*70)
    print("RECENT TRANSACTIONS")
    print("="*70)
    for log in library.transaction_log[-5:]:  # Last 5 transactions
        print(f"[{log['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}] {log['message']}")

    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
"""
Complex Library Management System
Demonstrates: Classes, Objects, Composition, Aggregation, Collections, Date handling
"""

from datetime import datetime, timedelta
from enum import Enum


class BookGenre(Enum):
    """Enum for book genres"""
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE = "Science"
    HISTORY = "History"
    BIOGRAPHY = "Biography"
    MYSTERY = "Mystery"
    FANTASY = "Fantasy"
    ROMANCE = "Romance"


class Book:
    """Represents a book in the library"""

    def __init__(self, isbn, title, author, genre, publication_year, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.borrowed_by = []  # List of member IDs who borrowed this book

    def is_available(self):
        return self.available_copies > 0

    def borrow(self, member_id):
        if self.is_available():
            self.available_copies -= 1
            self.borrowed_by.append(member_id)
            return True
        return False

    def return_book(self, member_id):
        if member_id in self.borrowed_by:
            self.available_copies += 1
            self.borrowed_by.remove(member_id)
            return True
        return False

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year}) - Available: {self.available_copies}/{self.total_copies}"


class Member:
    """Represents a library member"""

    member_id_counter = 1000

    def __init__(self, name, email, phone, membership_type="Regular"):
        self.member_id = Member.member_id_counter
        Member.member_id_counter += 1
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type  # Regular, Premium, Student
        self.registration_date = datetime.now()
        self.borrowed_books = {}  # {isbn: borrow_date}
        self.borrowing_history = []
        self.fines = 0.0

        # Different membership types have different limits
        self.max_books = {"Regular": 3, "Premium": 10, "Student": 5}[membership_type]
        self.borrow_duration = {"Regular": 14, "Premium": 30, "Student": 21}[membership_type]

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books and self.fines == 0

    def borrow_book(self, book):
        if not self.can_borrow():
            return False, "Cannot borrow: Limit reached or fines pending"

        if book.borrow(self.member_id):
            self.borrowed_books[book.isbn] = datetime.now()
            return True, f"Successfully borrowed '{book.title}'"
        return False, "Book not available"

    def return_book(self, book):
        if book.isbn not in self.borrowed_books:
            return False, "You haven't borrowed this book", 0

        borrow_date = self.borrowed_books[book.isbn]
        days_borrowed = (datetime.now() - borrow_date).days

        # Calculate fine if overdue
        fine = 0
        if days_borrowed > self.borrow_duration:
            overdue_days = days_borrowed - self.borrow_duration
            fine = overdue_days * 0.50  # $0.50 per day
            self.fines += fine

        book.return_book(self.member_id)
        del self.borrowed_books[book.isbn]

        # Add to history
        self.borrowing_history.append({
            "book": book.title,
            "borrow_date": borrow_date,
            "return_date": datetime.now(),
            "days": days_borrowed,
            "fine": fine
        })

        return True, f"Returned '{book.title}' after {days_borrowed} days", fine

    def pay_fine(self, amount):
        if amount >= self.fines:
            paid = self.fines
            self.fines = 0
            return True, f"Paid ${paid:.2f}. No pending fines."
        else:
            self.fines -= amount
            return True, f"Paid ${amount:.2f}. Remaining fine: ${self.fines:.2f}"

    def get_membership_duration(self):
        duration = datetime.now() - self.registration_date
        return duration.days

    def __str__(self):
        return (f"Member #{self.member_id}: {self.name} ({self.membership_type})\n"
                f"  Email: {self.email} | Phone: {self.phone}\n"
                f"  Books Borrowed: {len(self.borrowed_books)}/{self.max_books}\n"
                f"  Pending Fines: ${self.fines:.2f}\n"
                f"  Member for: {self.get_membership_duration()} days")


class Library:
    """Main library system that manages books and members"""

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = {}  # {isbn: Book}
        self.members = {}  # {member_id: Member}
        self.transaction_log = []

    def add_book(self, book):
        if book.isbn in self.books:
            # If book exists, increase copies
            self.books[book.isbn].total_copies += book.total_copies
            self.books[book.isbn].available_copies += book.total_copies
            return f"Added {book.total_copies} more copies of '{book.title}'"
        else:
            self.books[book.isbn] = book
            return f"New book added: '{book.title}'"

    def register_member(self, member):
        self.members[member.member_id] = member
        self.log_transaction(f"New member registered: {member.name} (ID: {member.member_id})")
        return member.member_id

    def find_book_by_title(self, title):
        results = []
        for book in self.books.values():
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def find_books_by_author(self, author):
        results = []
        for book in self.books.values():
            if author.lower() in book.author.lower():
                results.append(book)
        return results

    def find_books_by_genre(self, genre):
        results = []
        for book in self.books.values():
            if book.genre == genre:
                results.append(book)
        return results

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found"
        if isbn not in self.books:
            return False, "Book not found"

        member = self.members[member_id]
        book = self.books[isbn]

        success, message = member.borrow_book(book)
        if success:
            self.log_transaction(f"Member {member.name} borrowed '{book.title}'")
        return success, message

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found", 0
        if isbn not in self.books:
            return False, "Book not found", 0

        member = self.members[member_id]
        book = self.books[isbn]

        success, message, fine = member.return_book(book)
        if success:
            self.log_transaction(f"Member {member.name} returned '{book.title}'. Fine: ${fine:.2f}")
        return success, message, fine

    def log_transaction(self, message):
        self.transaction_log.append({
            "timestamp": datetime.now(),
            "message": message
        })

    def get_library_stats(self):
        total_books = sum(book.total_copies for book in self.books.values())
        available_books = sum(book.available_copies for book in self.books.values())
        borrowed_books = total_books - available_books
        total_fines = sum(member.fines for member in self.members.values())

        return {
            "total_books": total_books,
            "unique_titles": len(self.books),
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_members": len(self.members),
            "total_fines_pending": total_fines
        }

    def display_stats(self):
        stats = self.get_library_stats()
        print(f"\n{'='*60}")
        print(f"LIBRARY STATISTICS - {self.name}")
        print(f"{'='*60}")
        print(f"Total Books: {stats['total_books']} ({stats['unique_titles']} unique titles)")
        print(f"Available: {stats['available_books']} | Borrowed: {stats['borrowed_books']}")
        print(f"Total Members: {stats['total_members']}")
        print(f"Total Fines Pending: ${stats['total_fines_pending']:.2f}")
        print(f"{'='*60}\n")

    def display_all_books(self):
        print(f"\n--- All Books in {self.name} ---")
        for book in self.books.values():
            print(f"  [{book.isbn}] {book}")

    def display_all_members(self):
        print(f"\n--- All Members of {self.name} ---")
        for member in self.members.values():
            print(f"\n{member}")

    def __str__(self):
        return f"{self.name} Library\nLocation: {self.address}"


# ============================================
# DEMONSTRATION WITH COMPLEX OBJECTS
# ============================================

if __name__ == "__main__":
    print("="*70)
    print("COMPLEX LIBRARY MANAGEMENT SYSTEM")
    print("="*70)

    # Create Library
    library = Library("City Central Library", "123 Main Street, Downtown")
    print(f"\n{library}\n")

    # Create complex book objects
    book1 = Book("978-0-7432-7356-5", "1984", "George Orwell",
                 BookGenre.FICTION, 1949, 5)
    book2 = Book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee",
                 BookGenre.FICTION, 1960, 3)
    book3 = Book("978-0-553-29698-2", "A Brief History of Time", "Stephen Hawking",
                 BookGenre.SCIENCE, 1988, 4)
    book4 = Book("978-0-345-39180-3", "Dune", "Frank Herbert",
                 BookGenre.FANTASY, 1965, 2)
    book5 = Book("978-0-14-017739-8", "1984", "George Orwell",
                 BookGenre.FICTION, 1949, 3)  # Duplicate for testing

    # Add books to library
    print("\n--- Adding Books to Library ---")
    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))
    print(library.add_book(book4))
    print(library.add_book(book5))  # Will increase copies of existing book

    # Create complex member objects with different membership types
    member1 = Member("Alice Johnson", "alice@email.com", "555-0101", "Premium")
    member2 = Member("Bob Smith", "bob@email.com", "555-0102", "Regular")
    member3 = Member("Charlie Davis", "charlie@email.com", "555-0103", "Student")
    member4 = Member("Diana Prince", "diana@email.com", "555-0104", "Regular")

    # Register members
    print("\n--- Registering Members ---")
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)
    library.register_member(member4)
    print(f"Registered {len(library.members)} members")

    # Display initial state
    library.display_all_books()
    library.display_stats()

    # Simulate borrowing operations
    print("\n" + "="*70)
    print("BORROWING OPERATIONS")
    print("="*70)

    # Alice borrows multiple books (Premium member can borrow up to 10)
    print(f"\n--- {member1.name} (Premium Member) Borrowing ---")
    success, msg = library.borrow_book(member1.member_id, book1.isbn)
    print(msg)
    success, msg = library.borrow_book(member1.member_id, book3.isbn)
    print(msg)
    success, msg = library.borrow_book(member1.member_id, book4.isbn)
    print(msg)

    # Bob borrows books (Regular member can borrow up to 3)
    print(f"\n--- {member2.name} (Regular Member) Borrowing ---")
    success, msg = library.borrow_book(member2.member_id, book2.isbn)
    print(msg)
    success, msg = library.borrow_book(member2.member_id, book1.isbn)
    print(msg)

    # Charlie borrows books (Student member can borrow up to 5)
    print(f"\n--- {member3.name} (Student Member) Borrowing ---")
    success, msg = library.borrow_book(member3.member_id, book3.isbn)
    print(msg)

    # Display updated stats
    library.display_stats()

    # Search functionality
    print("\n" + "="*70)
    print("SEARCH OPERATIONS")
    print("="*70)

    print("\n--- Searching for '1984' ---")
    results = library.find_book_by_title("1984")
    for book in results:
        print(f"  Found: {book}")

    print("\n--- Searching for author 'Orwell' ---")
    results = library.find_books_by_author("Orwell")
    for book in results:
        print(f"  Found: {book}")

    print("\n--- All Fiction books ---")
    results = library.find_books_by_genre(BookGenre.FICTION)
    for book in results:
        print(f"  {book}")

    # Simulate returns with overdue fines
    print("\n" + "="*70)
    print("RETURN OPERATIONS")
    print("="*70)

    # Simulate overdue by manipulating borrow date
    print(f"\n--- Simulating overdue return for {member2.name} ---")
    member2.borrowed_books[book2.isbn] = datetime.now() - timedelta(days=20)  # 20 days ago
    success, msg, fine = library.return_book(member2.member_id, book2.isbn)
    print(msg)
    if fine > 0:
        print(f"  OVERDUE FINE: ${fine:.2f}")

    print(f"\n--- {member1.name} returning books (on time) ---")
    success, msg, fine = library.return_book(member1.member_id, book1.isbn)
    print(msg)

    # Display member information
    print("\n" + "="*70)
    print("MEMBER INFORMATION")
    print("="*70)
    library.display_all_members()

    # Pay fines
    print("\n" + "="*70)
    print("FINE PAYMENT")
    print("="*70)
    print(f"\n{member2.name} has ${member2.fines:.2f} in fines")
    success, msg = member2.pay_fine(5.0)
    print(msg)

    # Show borrowing history
    print("\n" + "="*70)
    print("BORROWING HISTORY")
    print("="*70)
    print(f"\n--- {member2.name}'s History ---")
    for record in member2.borrowing_history:
        print(f"  Book: {record['book']}")
        print(f"  Borrowed: {record['borrow_date'].strftime('%Y-%m-%d')}")
        print(f"  Returned: {record['return_date'].strftime('%Y-%m-%d')}")
        print(f"  Duration: {record['days']} days")
        print(f"  Fine: ${record['fine']:.2f}\n")

    # Final stats
    library.display_stats()

    # Transaction log
    print("\n" + "="*70)
    print("RECENT TRANSACTIONS")
    print("="*70)
    for log in library.transaction_log[-5:]:  # Last 5 transactions
        print(f"[{log['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}] {log['message']}")

    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
"""
Complex Library Management System
Demonstrates: Classes, Objects, Composition, Aggregation, Collections, Date handling
"""

from datetime import datetime, timedelta
from enum import Enum


class BookGenre(Enum):
    """Enum for book genres"""
    FICTION = "Fiction"
    NON_FICTION = "Non-Fiction"
    SCIENCE = "Science"
    HISTORY = "History"
    BIOGRAPHY = "Biography"
    MYSTERY = "Mystery"
    FANTASY = "Fantasy"
    ROMANCE = "Romance"


class Book:
    """Represents a book in the library"""

    def __init__(self, isbn, title, author, genre, publication_year, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.borrowed_by = []  # List of member IDs who borrowed this book

    def is_available(self):
        return self.available_copies > 0

    def borrow(self, member_id):
        if self.is_available():
            self.available_copies -= 1
            self.borrowed_by.append(member_id)
            return True
        return False

    def return_book(self, member_id):
        if member_id in self.borrowed_by:
            self.available_copies += 1
            self.borrowed_by.remove(member_id)
            return True
        return False

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year}) - Available: {self.available_copies}/{self.total_copies}"


class Member:
    """Represents a library member"""

    member_id_counter = 1000

    def __init__(self, name, email, phone, membership_type="Regular"):
        self.member_id = Member.member_id_counter
        Member.member_id_counter += 1
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_type = membership_type  # Regular, Premium, Student
        self.registration_date = datetime.now()
        self.borrowed_books = {}  # {isbn: borrow_date}
        self.borrowing_history = []
        self.fines = 0.0

        # Different membership types have different limits
        self.max_books = {"Regular": 3, "Premium": 10, "Student": 5}[membership_type]
        self.borrow_duration = {"Regular": 14, "Premium": 30, "Student": 21}[membership_type]

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books and self.fines == 0

    def borrow_book(self, book):
        if not self.can_borrow():
            return False, "Cannot borrow: Limit reached or fines pending"

        if book.borrow(self.member_id):
            self.borrowed_books[book.isbn] = datetime.now()
            return True, f"Successfully borrowed '{book.title}'"
        return False, "Book not available"

    def return_book(self, book):
        if book.isbn not in self.borrowed_books:
            return False, "You haven't borrowed this book", 0

        borrow_date = self.borrowed_books[book.isbn]
        days_borrowed = (datetime.now() - borrow_date).days

        # Calculate fine if overdue
        fine = 0
        if days_borrowed > self.borrow_duration:
            overdue_days = days_borrowed - self.borrow_duration
            fine = overdue_days * 0.50  # $0.50 per day
            self.fines += fine

        book.return_book(self.member_id)
        del self.borrowed_books[book.isbn]

        # Add to history
        self.borrowing_history.append({
            "book": book.title,
            "borrow_date": borrow_date,
            "return_date": datetime.now(),
            "days": days_borrowed,
            "fine": fine
        })

        return True, f"Returned '{book.title}' after {days_borrowed} days", fine

    def pay_fine(self, amount):
        if amount >= self.fines:
            paid = self.fines
            self.fines = 0
            return True, f"Paid ${paid:.2f}. No pending fines."
        else:
            self.fines -= amount
            return True, f"Paid ${amount:.2f}. Remaining fine: ${self.fines:.2f}"

    def get_membership_duration(self):
        duration = datetime.now() - self.registration_date
        return duration.days

    def __str__(self):
        return (f"Member #{self.member_id}: {self.name} ({self.membership_type})\n"
                f"  Email: {self.email} | Phone: {self.phone}\n"
                f"  Books Borrowed: {len(self.borrowed_books)}/{self.max_books}\n"
                f"  Pending Fines: ${self.fines:.2f}\n"
                f"  Member for: {self.get_membership_duration()} days")


class Library:
    """Main library system that manages books and members"""

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = {}  # {isbn: Book}
        self.members = {}  # {member_id: Member}
        self.transaction_log = []

    def add_book(self, book):
        if book.isbn in self.books:
            # If book exists, increase copies
            self.books[book.isbn].total_copies += book.total_copies
            self.books[book.isbn].available_copies += book.total_copies
            return f"Added {book.total_copies} more copies of '{book.title}'"
        else:
            self.books[book.isbn] = book
            return f"New book added: '{book.title}'"

    def register_member(self, member):
        self.members[member.member_id] = member
        self.log_transaction(f"New member registered: {member.name} (ID: {member.member_id})")
        return member.member_id

    def find_book_by_title(self, title):
        results = []
        for book in self.books.values():
            if title.lower() in book.title.lower():
                results.append(book)
        return results

    def find_books_by_author(self, author):
        results = []
        for book in self.books.values():
            if author.lower() in book.author.lower():
                results.append(book)
        return results

    def find_books_by_genre(self, genre):
        results = []
        for book in self.books.values():
            if book.genre == genre:
                results.append(book)
        return results

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found"
        if isbn not in self.books:
            return False, "Book not found"

        member = self.members[member_id]
        book = self.books[isbn]

        success, message = member.borrow_book(book)
        if success:
            self.log_transaction(f"Member {member.name} borrowed '{book.title}'")
        return success, message

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found", 0
        if isbn not in self.books:
            return False, "Book not found", 0

        member = self.members[member_id]
        book = self.books[isbn]

        success, message, fine = member.return_book(book)
        if success:
            self.log_transaction(f"Member {member.name} returned '{book.title}'. Fine: ${fine:.2f}")
        return success, message, fine

    def log_transaction(self, message):
        self.transaction_log.append({
            "timestamp": datetime.now(),
            "message": message
        })

    def get_library_stats(self):
        total_books = sum(book.total_copies for book in self.books.values())
        available_books = sum(book.available_copies for book in self.books.values())
        borrowed_books = total_books - available_books
        total_fines = sum(member.fines for member in self.members.values())

        return {
            "total_books": total_books,
            "unique_titles": len(self.books),
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_members": len(self.members),
            "total_fines_pending": total_fines
        }

    def display_stats(self):
        stats = self.get_library_stats()
        print(f"\n{'='*60}")
        print(f"LIBRARY STATISTICS - {self.name}")
        print(f"{'='*60}")
        print(f"Total Books: {stats['total_books']} ({stats['unique_titles']} unique titles)")
        print(f"Available: {stats['available_books']} | Borrowed: {stats['borrowed_books']}")
        print(f"Total Members: {stats['total_members']}")
        print(f"Total Fines Pending: ${stats['total_fines_pending']:.2f}")
        print(f"{'='*60}\n")

    def display_all_books(self):
        print(f"\n--- All Books in {self.name} ---")
        for book in self.books.values():
            print(f"  [{book.isbn}] {book}")

    def display_all_members(self):
        print(f"\n--- All Members of {self.name} ---")
        for member in self.members.values():
            print(f"\n{member}")

    def __str__(self):
        return f"{self.name} Library\nLocation: {self.address}"


# ============================================
# DEMONSTRATION WITH COMPLEX OBJECTS
# ============================================

if __name__ == "__main__":
    print("="*70)
    print("COMPLEX LIBRARY MANAGEMENT SYSTEM")
    print("="*70)

    # Create Library
    library = Library("City Central Library", "123 Main Street, Downtown")
    print(f"\n{library}\n")

    # Create complex book objects
    book1 = Book("978-0-7432-7356-5", "1984", "George Orwell",
                 BookGenre.FICTION, 1949, 5)
    book2 = Book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee",
                 BookGenre.FICTION, 1960, 3)
    book3 = Book("978-0-553-29698-2", "A Brief History of Time", "Stephen Hawking",
                 BookGenre.SCIENCE, 1988, 4)
    book4 = Book("978-0-345-39180-3", "Dune", "Frank Herbert",
                 BookGenre.FANTASY, 1965, 2)
    book5 = Book("978-0-14-017739-8", "1984", "George Orwell",
                 BookGenre.FICTION, 1949, 3)  # Duplicate for testing

    # Add books to library
    print("\n--- Adding Books to Library ---")
    print(library.add_book(book1))
    print(library.add_book(book2))
    print(library.add_book(book3))
    print(library.add_book(book4))
    print(library.add_book(book5))  # Will increase copies of existing book

    # Create complex member objects with different membership types
    member1 = Member("Alice Johnson", "alice@email.com", "555-0101", "Premium")
    member2 = Member("Bob Smith", "bob@email.com", "555-0102", "Regular")
    member3 = Member("Charlie Davis", "charlie@email.com", "555-0103", "Student")
    member4 = Member("Diana Prince", "diana@email.com", "555-0104", "Regular")

    # Register members
    print("\n--- Registering Members ---")
    library.register_member(member1)
    library.register_member(member2)
    library.register_member(member3)
    library.register_member(member4)
    print(f"Registered {len(library.members)} members")

    # Display initial state
    library.display_all_books()
    library.display_stats()

    # Simulate borrowing operations
    print("\n" + "="*70)
    print("BORROWING OPERATIONS")
    print("="*70)

    # Alice borrows multiple books (Premium member can borrow up to 10)
    print(f"\n--- {member1.name} (Premium Member) Borrowing ---")
    success, msg = library.borrow_book(member1.member_id, book1.isbn)
    print(msg)
    success, msg = library.borrow_book(member1.member_id, book3.isbn)
    print(msg)
    success, msg = library.borrow_book(member1.member_id, book4.isbn)
    print(msg)

    # Bob borrows books (Regular member can borrow up to 3)
    print(f"\n--- {member2.name} (Regular Member) Borrowing ---")
    success, msg = library.borrow_book(member2.member_id, book2.isbn)
    print(msg)
    success, msg = library.borrow_book(member2.member_id, book1.isbn)
    print(msg)

    # Charlie borrows books (Student member can borrow up to 5)
    print(f"\n--- {member3.name} (Student Member) Borrowing ---")
    success, msg = library.borrow_book(member3.member_id, book3.isbn)
    print(msg)

    # Display updated stats
    library.display_stats()

    # Search functionality
    print("\n" + "="*70)
    print("SEARCH OPERATIONS")
    print("="*70)

    print("\n--- Searching for '1984' ---")
    results = library.find_book_by_title("1984")
    for book in results:
        print(f"  Found: {book}")

    print("\n--- Searching for author 'Orwell' ---")
    results = library.find_books_by_author("Orwell")
    for book in results:
        print(f"  Found: {book}")

    print("\n--- All Fiction books ---")
    results = library.find_books_by_genre(BookGenre.FICTION)
    for book in results:
        print(f"  {book}")

    # Simulate returns with overdue fines
    print("\n" + "="*70)
    print("RETURN OPERATIONS")
    print("="*70)

    # Simulate overdue by manipulating borrow date
    print(f"\n--- Simulating overdue return for {member2.name} ---")
    member2.borrowed_books[book2.isbn] = datetime.now() - timedelta(days=20)  # 20 days ago
    success, msg, fine = library.return_book(member2.member_id, book2.isbn)
    print(msg)
    if fine > 0:
        print(f"  OVERDUE FINE: ${fine:.2f}")

    print(f"\n--- {member1.name} returning books (on time) ---")
    success, msg, fine = library.return_book(member1.member_id, book1.isbn)
    print(msg)

    # Display member information
    print("\n" + "="*70)
    print("MEMBER INFORMATION")
    print("="*70)
    library.display_all_members()

    # Pay fines
    print("\n" + "="*70)
    print("FINE PAYMENT")
    print("="*70)
    print(f"\n{member2.name} has ${member2.fines:.2f} in fines")
    success, msg = member2.pay_fine(5.0)
    print(msg)

    # Show borrowing history
    print("\n" + "="*70)
    print("BORROWING HISTORY")
    print("="*70)
    print(f"\n--- {member2.name}'s History ---")
    for record in member2.borrowing_history:
        print(f"  Book: {record['book']}")
        print(f"  Borrowed: {record['borrow_date'].strftime('%Y-%m-%d')}")
        print(f"  Returned: {record['return_date'].strftime('%Y-%m-%d')}")
        print(f"  Duration: {record['days']} days")
        print(f"  Fine: ${record['fine']:.2f}\n")

    # Final stats
    library.display_stats()

    # Transaction log
    print("\n" + "="*70)
    print("RECENT TRANSACTIONS")
    print("="*70)
    for log in library.transaction_log[-5:]:  # Last 5 transactions
        print(f"[{log['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}] {log['message']}")

    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
