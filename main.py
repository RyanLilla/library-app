import tkinter as tk
from tkinter import messagebox, ttk

from library import Library
from book import Book


def add_book():
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
    pass


library = Library()
library.load_books_from_file()

window = tk.Tk()
window.title("Library-App")

# book title - label and entry
label_book_title = tk.Label(window, text="Title:")
label_book_title.grid(row=0, column=0)
entry_book_title = tk.Entry(window)
entry_book_title.grid(row=0, column=1)

# author - label and entry
label_author_name = tk.Label(window, text="Author:")
label_author_name.grid(row=1, column=0)
entry_author_name = tk.Entry(window)
entry_author_name.grid(row=1, column=1)

# buttons
button_add = tk.Button(window, text="Add Book")
button_add.grid(row=2, column=0)
button_remove = tk.Button(window, text="Remove Book")
button_remove.grid(row=2, column=1)

# table to display the list of books
book_table = ttk.Treeview(window, columns=("Title", "Author"), show="headings")
book_table.heading(column="Title", text="Title")
book_table.heading(column="Author", text="Author")
book_table.grid(row=3, column=0, columnspan=2)

update_book_table()

window.mainloop()