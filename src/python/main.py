import tkinter as tk
from tkinter import filedialog
import os
from ctypes import cdll


root = tk.Tk()

root.title("PDF searcher")
root.geometry("700x400")
script_dir = os.path.dirname(os.path.abspath(__file__))
root.wm_iconbitmap(os.path.join(script_dir, "icon.ico"))
root.resizable(0,0)


screen_width = root.winfo_screenwidth()

screen_height = root.winfo_screenheight()

x = (screen_width/2) - (700/2)

y = (screen_height/2) - (400/2)

root.geometry("%dx%d+%d+%d" % (700, 400, x, y))

documents_folder = os.path.expanduser("~/Documents").replace("\\", "/")

#create a label

title = tk.Label(root, text="Z_Ninja_Monkey's OCR PDF Searcher", font=("Helvetica", 15))
#place title using .place in the top center of the screen

title.place(x=0, y=10, relwidth=1)

#create a typing box with a lable and a button. Place the box in the middle of the screen. button opens a menu to look through and select a file, then the selected file is put into the typing box automatically

file_selector_box = tk.Entry(root, font=("Helvetica", 10))

file_selector_box.insert(0, documents_folder)

file_selector_box.place(x=250, y=70, width=300, height=28)

#create a button to open a file explorer to select a file

def open_folder_selector():
    file_path = filedialog.askdirectory(initialdir=documents_folder, title="Select a folder to Scan")
    file_selector_box.delete(0, tk.END)
    file_selector_box.insert(0, file_path)

    
folder_selector_button = tk.Button(root, text="Select Folder", font=("Helvetica", 10), command=open_folder_selector)

folder_selector_button.place(x=155, y=70)


search_keyword_box = tk.Entry(root, font=("Helvetica", 10))

search_keyword_box.place(x=125, y=160, width=450, height=35)

placeholder_text = "Enter Search Keywords, Separated by Commas"

def show_placeholder(event):
    if not search_keyword_box.get():
        search_keyword_box.insert(0, placeholder_text)
        search_keyword_box.config(fg="grey")

def hide_placeholder(event):
    if search_keyword_box.get() == placeholder_text:
        search_keyword_box.delete(0, tk.END)
        search_keyword_box.config(fg="black")

search_keyword_box.insert(0, placeholder_text)
search_keyword_box.config(fg="grey")
search_keyword_box.bind("<FocusIn>", hide_placeholder)
search_keyword_box.bind("<FocusOut>", show_placeholder)

def search():
    lib = cdll.LoadLibrary(os.path.join(script_dir, "ocr_searcher.dll"))
    progress = lib.getProgress()
    print(progress)
    

search_button = tk.Button(root, text="Search!", font=("Helvetica", 15), command=search)

search_button.place(x=200, y=250, width=300, height=100)
search_button.config(background="#ebebeb", fg="black")

root.mainloop()
