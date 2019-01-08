from tkinter import *

# Create a dialog with an input box and a button for user inputs
root = Tk()
root.title("Keyword Locator")

# Path entry
path_label = Label(root, text="Enter the absolute path for a directory:")
path_entry = Entry(root)
path_label.grid(row=0, column=0)
path_entry.grid(row=0, column=1)

# Keyword entry
kw_label = Label(root, text="Enter the keyword:")
kw_entry = Entry(root)
kw_label.grid(row=1, column=0)
kw_entry.grid(row=1, column=1)

# Buttons
submit_btn = Button(root, text="Search")
exit_btn = Button(root, text="Cancel")
submit_btn.grid(row=2, column=0)
exit_btn.grid(row=2, column=1)

root.mainloop()

# TODO: click events