
class Book:
    # Constructor
    def __init__(self, title : str, author : str, ISBN : str = None, available : bool = False ):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

my_book = Book("10 años de soledad", "Gabriel Garcia Marquez")
second_book = Book("Cuando soñe sercientifica","Carmen Garcia Lizarraga")
third_book = Book("Libro 3", "Eric RG", ISBN="ISBN-12345", available=True)

list_of_books = [my_book, second_book]
list_of_books.append(third_book)
index = 1

for book in list_of_books:
    print(f"""{index}.- {book.title} - {book.author} - 
          Available = {book.available}, ISBN = {book.ISBN}""")
    index += 1

