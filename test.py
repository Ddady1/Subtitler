import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter import messagebox
from ctypes import windll
import os
import json
windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'


def choose_files():
    #filetypes = ('All files', '*.*')
    files = fd.askopenfilenames(parent=root, title='Choose files')#, filetypes=filetypes)
    #messagebox.askquestion(title='Selected files', message='Do you wish to continue?')
    file = ''
    subline = []
    sublines = []
    for item in files:
        file += item
    with open(file, 'r') as f:
        con = f.readlines()
    for item in con:
        if item != '\n':
            subline.append(item)
        else:
            sublines.append(subline)
            subline = []

    print(sublines)
    #for ln in con:
    #    print(ln)


    #print(lines)
    #i = 1
    #for line in lines:
    #    files_listbox.insert(i, line)
    #    i += 1



root = tk.Tk()
root.title('Set .ass Subtitle')
root.geometry('458x600+350+150')

choosefiles_button = tk.Button(root, text='Choose Files', foreground=text_color, font=('Ariel', 12, 'bold'),\
                               command=lambda: choose_files())
choosefiles_button.place(x=20, y=400, width=120)


fileslist_label = ttk.Label(root, text='Selected files:', foreground=text_color, font=('Ariel', 11, 'bold'))
fileslist_label.place(x=240, y=400)
files_listbox = tk.Listbox(root)
files_listbox.place(x=150, y=420, width=288, height=170)


root.mainloop()
