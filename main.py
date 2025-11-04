
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
        return self.__times_borrowed > 5 

    # Getter
    def get_times_borrowed(self):
        return self.__times_borrowed
    
    # Setter
    def set_times_borrowed(self, value):
        self.__times_borrowed = value

my_book =       Book("10 años de soledad", "Gabriel Garcia Marquez",available=True)
second_book =   Book("Cuando soñe sercientifica","Carmen Garcia Lizarraga", available=True)
third_book =    Book("Libro 3", "Eric RG", ISBN="ISBN-12345", available=True)

# Cambiar el estado available de un libro
print(my_book.borrow_book())
print(my_book.return_book())

list_of_books = [my_book, second_book]
list_of_books.append(third_book)

for book in list_of_books:
    print(book)
    book.is_popular()
    

