
class Library:
    def __init__(self, name: str):
        self.name = name
        self.books : list[Book] = []
        self.users : list[User] = []
        
    def books_available(self):
        # List Comprehension
        return [b.title for b in self.books if b.available]