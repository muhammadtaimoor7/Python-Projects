#LIBRARY MANAGEMENT SYSTEM PROJECT 
# USING OOP METHODS
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # True = available, False = issued

    def show_details(self): 

        if self.available:#means yes # no self.means not there
            status = "Available"
        else:
            status = "Issued"
        print(f"Book: {self.title} by {self.author} - {status}")

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"You have issued '{self.title}'")
        else:
            print(f"Sorry, '{self.title}' is already issued")

    def return_book(self):
        if not self.available:  # only return if issued
            self.available = True
            print(f"'{self.title}' has been returned")
        else:
            print(f"'{self.title}' was not issued")

#  Member Classes
class Member:  # parent class
    def __init__(self, name, unique_id):
        self.name = name
        self.unique_id = unique_id

    def show_member(self):
        print(f"{self.name} has ID: {self.unique_id}")

class StudentMember(Member):
    def __init__(self, name, unique_id, grade):
        self.name = name
        self.unique_id = unique_id
        self.grade = grade

class TeacherMember(Member):
    def __init__(self, name, unique_id, subject):
        self.name = name
        self.unique_id = unique_id
        self.subject = subject

# Library Class
class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_members = []

    def add_book(self, book):
        self.list_of_books.append(book)
        print(f"Book '{book.title}' added to library")

    def add_member(self, member):
        self.list_of_members.append(member)
        print(f"Member '{member.name}' added to library with ID {member.unique_id}")

    def issue_book(self, member, book_title):
        for book in self.list_of_books:
            if book.title == book_title:
                if book.available:
                    book.issue_book()
                    print(f"{member.name} has been issued '{book.title}'")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already issued")
                    return
        print(f"Book '{book_title}' not found in library")

    def return_book(self, book_title):
        for book in self.list_of_books:
            if book.title == book_title:
                if not book.available:
                    book.return_book()
                    return
                else:
                    print(f"'{book.title}' was not issued")
                    return
        print(f"Book '{book_title}' not found in library")

    def show_all_books(self):
        if not self.list_of_books:
            print("No books in library")
        else:
            print("Books in library:")
            for book in self.list_of_books:
                book.show_details()


# OBJECTS 
lib = Library()  # Library create karna

#  Book Objects
b1 = Book("Python Basics", "Ali")
b2 = Book("Data Science 101", "Sara")
b3 = Book("AI Introduction", "Usman")

# Adding Books to Library
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

#  StudentMember Objects 
s1 = StudentMember("Ali", 101, "10th Grade")
s2 = StudentMember("Sara", 102, "9th Grade")

#  TeacherMember Objects 
t1 = TeacherMember("Mr. Ahmed", 201, "Math")
t2 = TeacherMember("Mrs. Sana", 202, "Physics")

# Adding Members to Library
lib.add_member(s1)
lib.add_member(s2)
lib.add_member(t1)
lib.add_member(t2)
#Issue Books
lib.issue_book(s1, "Python Basics")  
lib.issue_book(s2, "Data Science 101") 
lib.issue_book(s1, "Python Basics")   

# - Show All Books
lib.show_all_books()  # Library ki sari books ka status dikhayega

#-- Return Books
lib.return_book("Python Basics") 
lib.return_book("AI Introduction")

# - Show All Books Again 
lib.show_all_books()  # Updated status of all books

