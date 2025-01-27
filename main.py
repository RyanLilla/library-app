import tkinter as tk
from tkinter import messagebox, ttk

from library import Library
from book import Book


def add_book():
    """
    Adds a new book to the library.

    Retrieves the title and author from the input fields, creates a new Book object,
    adds it to the library, and updates the book table. Displays a success message
    if the book is added successfully, otherwise shows an error message.
    """
    
    title = entry_book_title.get()
    author = entry_author_name.get()
    
    if title and author:
        book = Book(title, author)
        library.add_book(book)
        
        messagebox.showinfo("Success", "Book add to library.")
        
        entry_book_title.delete(0, tk.END)
        entry_author_name.delete(0, tk.END)
        
        update_book_table()
    else:
        messagebox.showerror("Error", "Please enter a title and author.")

def remove_book():
    """
    Removes selected books from the library.

    Retrieves the selected books from the book table, removes each book from the library,
    deletes the book from the table, and updates the book table. Displays an error message
    if no books are selected.
    """
    
    selected_books = book_table.selection()
    if selected_books:
        for selected in selected_books:
            book = (book_table.item(selected, "values")[0], book_table.item(selected, "values")[1])
            library.remove_book(Book(book[0], book[1]))
            book_table.delete(selected)
        update_book_table()
    else:
        messagebox.showerror("Error", "Please select at least one book to remove.")
            

def update_book_table():
    """
    Updates the book table with the current list of books in the library.

    Clears the existing entries in the book table and repopulates it with the
    updated list of books from the library.
    """
    
    # Get the current books in the table
    current_books = set((book_table.item(item, "values")[0], book_table.item(item, "values")[1]) for item in book_table.get_children())
    
    # Get the books in the library
    library_books = set((book.title, book.author) for book in library.list_books())
    
    # Remove the books that are no longer in the library
    books_to_remove = current_books - library_books
    books_to_add = library_books - current_books
    for book in books_to_remove:
        book_table.delete(book)
    
    # Add the new books to the table
    for book in books_to_add:
        book_table.insert("", "end", values=book)


library = Library()
library.load_books_from_file()

window = tk.Tk()
window.title("Library-App")
window.geometry("400x300")  # Set initial size
window.resizable(True, True)  # Allow resizing

# Configure grid weights to make elements resize with the window
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# book title - label and entry
label_book_title = tk.Label(window, text="Title:")
label_book_title.grid(row=0, column=0, sticky="nsew")
entry_book_title = tk.Entry(window)
entry_book_title.grid(row=0, column=1, sticky="nsew")

# author - label and entry
label_author_name = tk.Label(window, text="Author:")
label_author_name.grid(row=1, column=0, sticky="nsew")
entry_author_name = tk.Entry(window)
entry_author_name.grid(row=1, column=1, sticky="nsew")

# buttons
button_add = tk.Button(window, text="Add Book", command=add_book)
button_add.grid(row=2, column=0, sticky="nsew")
button_remove = tk.Button(window, text="Remove Book", command=remove_book)
button_remove.grid(row=2, column=1, sticky="nsew")

# table to display the list of books
book_table = ttk.Treeview(window, columns=("Title", "Author"), show="headings")
book_table.heading(column="Title", text="Title")
book_table.heading(column="Author", text="Author")
book_table.grid(row=3, column=0, columnspan=2, sticky="nsew")

update_book_table()

window.mainloop()