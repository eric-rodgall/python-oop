
from books import Book
from library import Library
from users import Student, Teacher, RequestProtocol

my_book =       Book("10 años de soledad", "Gabriel Garcia Marquez",available=True)
second_book =   Book("Cuando soñe sercientifica","Carmen Garcia Lizarraga", available=True)
third_book =    Book("Python 101", "Eric RG", ISBN="ISBN-12345", available=False)

library = Library("Albany Library")

student = Student("Eric", "E1", "ISC")
student_2 = Student("Juan", "E2", "ISC")
teacher = Teacher("Carmen", "T1", "IE")

users : list[RequestProtocol] = [student, student_2, teacher] 

# for user in users : 
#     print(user.borrow_book("python 101"))

library.books = [my_book, second_book, third_book]
print(library.books_available())


