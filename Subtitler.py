import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter.messagebox import showinfo, askyesno
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'


def choose_files():
    filez = fd.askopenfilenames(parent=root, title='Choose a file')


def menu_about():
    showinfo(title='ABout', message='Replace .ass ver. 1.0.0\nBy David Hay Racha')


# Create the main window

root = tk.Tk()
root.title('Set .ass Subtitle')
root.geometry('600x500+150+150')
#root.iconbitmap('assets/reminder.ico')


# Create variables

Name = tk.StringVar()
Fontname = tk.StringVar()
Fontsize = tk.StringVar()
PrimaryColour = tk.StringVar()
SecondaryColour = tk.StringVar()
OutlineColour = tk.StringVar()
BackColour = tk.StringVar()
Bold = tk.StringVar()
Italic = tk.StringVar()
Underline = tk.StringVar()
StrikeOut = tk.StringVar()
ScaleX = tk.StringVar()
ScaleY = tk.StringVar()
Spacing = tk.StringVar()
Angle = tk.StringVar()
BorderStyle = tk.StringVar()
Outline = tk.StringVar()
Shadow = tk.StringVar()
Alignment = tk.StringVar()
MarginL = tk.StringVar()
MarginR = tk.StringVar()
MarginV = tk.StringVar()
Encoding = tk.StringVar()

# Create Main Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create File Menu

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Save as Default')
file_menu.add_separator()
file_menu.add_command(label='Change')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Create Help Menu

help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=menu_about)
















root.mainloop()

