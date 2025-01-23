from book import Book


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        self.save_books_to_file()
    
    def remove_book(self, book):
        self.books = [b for b in self.books if b.title != book.title or b.author != book.author]
    
    def list_books(self):
        return self.books
    
    def save_books_to_file(self):
        with open("library.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author}\n")
    
    def load_books_from_file(self):
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    title, author = line.strip().split(",")
                    book = Book(title, author)
                    self.books.append(book)
        except FileNotFoundError:
            pass