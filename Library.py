from book import Book


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """
        Adds a book to the library and saves the updated list to a file.

        Args:
            book (Book): The book to add to the library.
        """
        
        self.books.append(book)
        self.save_books_to_file()
    
    def remove_book(self, book):
        """
        Removes a book from the library.

        Args:
            book (Book): The book to remove from the library.
        """
        
        self.books = [b for b in self.books if b.title != book.title or b.author != book.author]
        self.save_books_to_file()
    
    def list_books(self):
        """
        Returns the list of books in the library.

        Returns:
            list: The list of books in the library.
        """
        
        return self.books
    
    def save_books_to_file(self):
        """
        Saves the list of books to a file named 'library.txt'.
        """
        
        with open("library.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author}\n")
    
    def load_books_from_file(self):
        """
        Loads the list of books from a file named 'library.txt'.
        """
        
        try:
            with open("library.txt", "r") as file:
                for line in file:
                    title, author = line.strip().split(",")
                    book = Book(title, author)
                    self.books.append(book)
        except FileNotFoundError:
            pass