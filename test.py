import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter import messagebox
from ctypes import windll
import os
import json
windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'

def trimlinenum(line):
    line.pop(0)
    print(line)
    return line

def timeline(line):
    start = str(line[1:11])
    start = start.replace(',', '.')
    end = str(line[18:28])
    end = end.replace(',', '.')
    #print(start, end)
    return start, end

def get_text(line):

    line = (''.join(line))
    line = line.rstrip()
    return line.replace('\n', '\\N')


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

    print(sublines[5])
    asssub = ''
    sub_start = 'Dialogue: 0'
    sub_Stime = ''
    sub_Etime = ''
    sub_text = ''
    line = trimlinenum(sublines[5])
    sub_Stime, sub_Etime = timeline(line[0])
    sub_text = get_text(line[1:len(line)])

    asssub = f'{sub_start},{sub_Stime},{sub_Etime},Default,,0000,0000,0000,,{sub_text}'
    print(asssub)



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
