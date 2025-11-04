from typing import Protocol

# Crea un contrato que todos las clases deben cumplir
class RequestProtocol(Protocol): 
    # Se define el metodo que se tiene que definir en cada clase
    def borrow_book(self, title : str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...

class User:
    def __init__(self, name : str, id : str ):
        self.name = name
        self.id = id
        self.books_borrowed = []

    def borrow_book(self, title : str):
        return f"Request to borrow {title} by user {self.name}"

class Student(User):
    def __init__(self, name, id, carer : str):
        super().__init__(name, id)
        self.carer = carer
        self.max_books = 3

    def borrow_book(self, title : str):
        if len(self.books_borrowed) < self.max_books :
            self.books_borrowed.append(title)
            return f"Request to borrow {title} by user {self.name}"
        return f"Max book borrowed achieve"

    def return_book(self, title):
        if title in self.books_borrowed :
            self.books_borrowed.remove(title)
            return f"{title} returned by user {self.name}"
        return f"{title} not found in borrowed books by user {self.name}"

class Teacher(User):
    def __init__(self, name, id, carer : str):
        super().__init__(name, id)
        self.carer = carer
        self.max_books = None

    def borrow_book(self, title):
        self.books_borrowed.append(title)
        return f"Request to borrow {title} by user {self.name}"
    

student = Student("Eric", "E1", "ISC")
teacher = Teacher("Carmen", "T1", "IE")

print(student.borrow_book("python 101"))
print(student.borrow_book("python 102"))
print(student.borrow_book("python 103"))
print(student.borrow_book("python 104"))

print(student.return_book("python 102"))

