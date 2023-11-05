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
root.geometry('480x600+350+150')
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

# main window label

main_label = ttk.Label(root, text='Change .ass subtitle style', foreground=text_color, font=('Ariel', 14, 'bold'))
main_label.place(x=100, y=10)


# name label and entry

name_label = ttk.Label(root, text='Name:', foreground=text_color, font=('Ariel', 10))
name_label.place(x=20, y=50)
name_entry = ttk.Entry(root, textvariable=Name)
name_entry.place(x=20, y=70, width=200)
name_entry.focus()


# font name label and entry

fontname_label = ttk.Label(root, text='Font Name:', foreground=text_color, font=('Ariel', 10))
fontname_label.place(x=250, y=50)
fontname_entry = ttk.Entry(root, textvariable=Fontname)
fontname_entry.place(x=250, y=70, width=200)


# font size label and entry

fontsize_label = ttk.Label(root, text='Font Size:', foreground=text_color, font=('Ariel', 10))
fontsize_label.place(x=20, y=100)
fontsize_entry = ttk.Entry(root, textvariable=Fontsize)
fontsize_entry.place(x=20, y=120, width=61, )


# primary color label and entry

primarycolor_label = ttk.Label(root, text='Primary Color:', foreground=text_color, font=('Ariel', 10))
primarycolor_label.place(x=100, y=100)
primarycolor_entry = ttk.Entry(root, textvariable=PrimaryColour)
primarycolor_entry.place(x=100, y=120, width=84)


# secondary color label and entry

secondarycolor_label = ttk.Label(root, text='Secondary Color:', foreground=text_color, font=('Ariel', 10))
secondarycolor_label.place(x=200, y=100)
secondarycolor_entry = ttk.Entry(root, textvariable=SecondaryColour)
secondarycolor_entry.place(x=200, y=120, width=101)
















root.mainloop()

