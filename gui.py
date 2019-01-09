from tkinter import *
from pptx import Presentation
import sys, os

# Create a dialog with an input box and a button for user inputs
root = Tk()
root.title("Keyword Locator")

def search():
    directory = path_entry.get()
    keyword = kw_entry.get()
    if not directory or not keyword:
        insuf_input_label.grid(row=2, column=0)
    if not directory.endswith("/") or not directory.endswith("/"):
        invalid_dir_label.grid(row=2, column=0)
    files = os.listdir(directory)
    text_runs = []
    for file in files:
        if file.endswith('.pptx'):
            the_file = Presentation(directory + file)
            i = 0
            for slide in the_file.slides:
                i = i+1
                for shape in slide.shapes:
                    if not shape.has_text_frame:
                        continue
                    for paragraph in shape.text_frame.paragraphs:
                        for run in paragraph.runs:
                            if run.text.find(keyword) != -1:
                                text_runs.append(file+"-slide "+str(i))


    for x in text_runs:
        print(x)


def cancel():
    sys.exit()

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

# Error message
insuf_input_errormsg = "Insufficient input. Try again."
insuf_input_label = Label(root, text=insuf_input_errormsg, fg="red")
invalid_dir_errormsg = "Missing '/' or '\\' at the end of the directory path. Try again."
invalid_dir_label = Label(root, text=invalid_dir_errormsg, fg="red")


# Buttons
submit_btn = Button(root, text="Search", command=search)
exit_btn = Button(root, text="Cancel", command=exit)
submit_btn.grid(row=3, column=0)
exit_btn.grid(row=3, column=1)

root.mainloop()
