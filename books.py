from typing import Protocol

class RequestBookProtocol(Protocol):
    def borrow_book(self, title : str) -> str:
        """Metodo que debe implementar cualquier solicitante"""
        ...

    def return_bool(self, title : str ) -> str:
        """Regresar libros"""
        ...

    def calculate_duration(self) -> str :
        """Calcular duracion"""
        ...

class Book:
    # Constructor
    def __init__(self, title : str, author : str, ISBN : str = None, available : bool = False):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available
        self.__times_borrowed = 0

    # Metodo __str__ para personalizar una texto cuando imprimimos el objeto
    def __str__(self):
        response = f"{self.title} - {self.author} - 'Available = {self.available}, times borrowed = {self.__times_borrowed}"
        return response

    # Metodos de instancia
    def borrow_book(self):
        if self.available:
            self.available = False
            self.__times_borrowed += 1
            return f"{self.title} as been borrowed, times borrowed = {self.__times_borrowed}"
        return f"{self.title} is unavailable."

    def return_book(self):
        if not self.available:
            self.available = True
        return f"{self.title} is available."
    
    def is_popular(self):
        if self.__times_borrowed > 5:
            return f"* El titulo es popular" 
        return f"No es popular"

    # Getter
    def get_times_borrowed(self):
        return self.__times_borrowed
    
    # Setter
    def set_times_borrowed(self, value):
        self.__times_borrowed = value


class FisicBook(Book):
    def calculate_duration(self):
        return "7 days"


class EBook(Book):
    def calculate_duration(self):
        return "14 days" 
