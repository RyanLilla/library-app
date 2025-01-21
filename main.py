import tkinter as tk
from tkinter import messagebox, ttk

window = tk.Tk()
window.title("Library-App")

# title - label and entry
title_label = tk.Label(window, text="Title")
title_label.grid(row=0, column=0)
title_entry = tk.Entry(window)
title_entry.grid(row=0, column=1)

# author - label and entry
author_label = tk.Label(window, text="Author")
author_label.grid(row=1, column=0)
author_entry = tk.Entry(window)
author_entry.grid(row=1, column=1)

# buttons

# table to display the list of books


window.mainloop()
