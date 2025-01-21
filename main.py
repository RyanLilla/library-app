import tkinter as tk
from tkinter import messagebox, ttk

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


window.mainloop()
