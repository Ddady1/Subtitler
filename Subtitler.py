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
    filetypes = (('.ass files', '*.ass'), ('All files', '*.*'))
    files = fd.askopenfilenames(parent=root, title='Choose files', filetypes=filetypes)
    #messagebox.askquestion(title='Selected files', message='Do you wish to continue?')
    i = 1
    for file in files:
        files_listbox.insert(i, file)
        i += 1


def menu_about():
    messagebox.showinfo(title='ABout', message='Replace .ass ver. 1.0.0\nBy David Hay Racha')


def clear_fields(entry_list):
    for entry in entry_list:
        entry.delete(0, 'end')
    name_entry.focus()


def clear_selected():
    files_listbox.delete(0, 'end')


def checkbox_check(chk_var):
    if chk_var.get() == 1:
        return True
    return False


def submit(chk_var):
    chk_box_result = checkbox_check(chk_var)
    if chk_box_result:
        create_json(var_list, entry_list)
    change_files(entry_list)

    ## for checking ## print(chk_box_result)


def check_json():
    json_path = 'defaults.json'
    if os.path.isfile(json_path):
        return 'normal'
    return 'disabled'


def create_json(var_list, entry_list):
    json_exist = check_json()
    if json_exist == 'normal':
        answer = messagebox.askquestion('Defaults exists', 'The Defaults settings file already exists.'
                                                  ' Are you sure you want to Over-Write it?\n'
                               'Over-Writing it will ERASE all previous settings!', icon='warning')
        if answer == 'yes':
            json_dict = {}
            i = 0
            for entry in entry_list:
                con = entry.get()
                json_dict[var_list[i]] = con
                i += 1
            js_object = json.dumps(json_dict, indent=4)
            with open('defaults.json', 'w') as f:
                f.write(js_object)
        else:
            return


def open_file(file_path, ass_string):
    with open(file_path, 'w') as asf:
        asf.readlines()


def change_files(entry_list):
    ass_format = ''
    for entry in entry_list:
        ass_format += (entry.get() + ',')
    ## test ## print(ass_format)
    file_num = files_listbox.size()
    for i in range(file_num):
        open_file(files_listbox.get(i), ass_format)
        ## test ## print(files_listbox.get(i))






# Create the main window

root = tk.Tk()
root.title('Set .ass Subtitle')
root.geometry('458x600+350+150')
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
setasdefault = tk.IntVar()

var_list = ['Name', 'Fontname', 'Fontsize', 'PrimaryColour', 'SecondaryColour', 'OutlineColour', 'BackColour', 'Bold',
            'Italic', 'Underline', 'StrikeOut', 'ScaleX', 'ScaleY', 'Spacing', 'Angle', 'BorderStyle', 'Outline',
            'Shadow', 'Alignment', 'MarginL', 'MarginR', 'MarginV', 'Encoding']

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
name_entry.place(x=20, y=70)
name_entry.focus()


# font name label and entry

fontname_label = ttk.Label(root, text='Font Name:', foreground=text_color, font=('Ariel', 10))
fontname_label.place(x=166, y=50)
fontname_entry = ttk.Entry(root, textvariable=Fontname)
fontname_entry.place(x=166, y=70)


# font size label and entry

fontsize_label = ttk.Label(root, text='Font Size:', foreground=text_color, font=('Ariel', 10))
fontsize_label.place(x=312, y=50)
fontsize_entry = ttk.Entry(root, textvariable=Fontsize)
fontsize_entry.place(x=312, y=70)#, width=61)


# primary color label and entry

primarycolor_label = ttk.Label(root, text='Primary Color:', foreground=text_color, font=('Ariel', 10))
primarycolor_label.place(x=20, y=100)
primarycolor_entry = ttk.Entry(root, textvariable=PrimaryColour)
primarycolor_entry.place(x=20, y=120, width=89.5)


# secondary color label and entry

secondarycolor_label = ttk.Label(root, text='Secondary Color:', foreground=text_color, font=('Ariel', 10))
secondarycolor_label.place(x=129.5, y=100)
secondarycolor_entry = ttk.Entry(root, textvariable=SecondaryColour)
secondarycolor_entry.place(x=129.5, y=120, width=89.5)


# outline color label and entry

outlinecolor_label = ttk.Label(root, text='Outline Color:', foreground=text_color, font=('Ariel', 10))
outlinecolor_label.place(x=239, y=100)
outlinecolor_entry = ttk.Entry(root, textvariable=OutlineColour)
outlinecolor_entry.place(x=239, y=120, width=89.5)


# back coloe label and entry

backcolor_label = ttk.Label(root, text='Back Color:', foreground=text_color, font=('Ariel', 10))
backcolor_label.place(x=348.5, y=100)
backcolor_entry = ttk.Entry(root, textvariable=BackColour)
backcolor_entry.place(x=348.5, y=120, width=89.5)


# bold label and entry

bold_label = ttk.Label(root, text='Bold:', foreground=text_color, font=('Ariel', 10))
bold_label.place(x=20, y=150)
bold_entry = ttk.Entry(root, textvariable=Bold)
bold_entry.place(x=20, y=170, width=89.5)


# italic label and entry

italic_label = ttk.Label(root, text='Italic:', foreground=text_color, font=('Ariel', 10))
italic_label.place(x=129.5, y=150)
italic_entry = ttk.Entry(root, textvariable=Italic)
italic_entry.place(x=129.5, y=170, width=89.5)


# under line label and entry

underline_label = ttk.Label(root, text='Underline:', foreground=text_color, font=('Ariel', 10))
underline_label.place(x=239, y=150)
underline_entry = ttk.Entry(root, textvariable=Underline)
underline_entry.place(x=239, y=170, width=89.5)


# strikeout label and entry

strikeout_label = ttk.Label(root, text='Strikeout:', foreground=text_color, font=('Ariel', 10))
strikeout_label.place(x=348.5, y=150)
strikeout_entry = ttk.Entry(root, textvariable=StrikeOut)
strikeout_entry.place(x=348.5, y=170, width=89.5)


# scaleX label and entry

scalex_label = ttk.Label(root, text='ScaleX:', foreground=text_color, font=('Ariel', 10))
scalex_label.place(x=20, y=200)
scalex_entry = ttk.Entry(root, textvariable=ScaleX)
scalex_entry.place(x=20, y=220, width=89.5)


# scaleY label and entry

scaley_label = ttk.Label(root, text='ScaleY:', foreground=text_color, font=('Ariel', 10))
scaley_label.place(x=129.5, y=200)
scaley_entry = ttk.Entry(root, textvariable=ScaleY)
scaley_entry.place(x=129.5, y=220, width=89.5)


# spacing label and entry

spacing_label = ttk.Label(root, text='Spacing:', foreground=text_color, font=('Ariel', 10))
spacing_label.place(x=239, y=200)
spacing_entry = ttk.Entry(root, textvariable=Spacing)
spacing_entry.place(x=239, y=220, width=89.5)


# angel label and entry

angel_label = ttk.Label(root, text='Angel:', foreground=text_color, font=('Ariel', 10))
angel_label.place(x=348.5, y=200)
angel_entry = ttk.Entry(root, textvariable=Angle)
angel_entry.place(x=348.5, y=220, width=89.5)


# border style label and entry

borderstyle_label = ttk.Label(root, text='Border Style:', foreground=text_color, font=('Ariel', 10))
borderstyle_label.place(x=20, y=250)
borderstyle_entry = ttk.Entry(root, textvariable=BorderStyle)
borderstyle_entry.place(x=20, y=270, width=89.5)


# outline label and entry

outline_label = ttk.Label(root, text='Outline:', foreground=text_color, font=('Ariel', 10))
outline_label.place(x=129.5, y=250)
outline_entry = ttk.Entry(root, textvariable=Outline)
outline_entry.place(x=129.5, y=270, width=89.5)


# shadow label and entry

shadow_label = ttk.Label(root, text='Shadow:', foreground=text_color, font=('Ariel', 10))
shadow_label.place(x=239, y=250)
shadow_entry = ttk.Entry(root, textvariable=Shadow)
shadow_entry.place(x=239, y=270, width=89.5)


# alignment label and entry

alignment_label = ttk.Label(root, text='Alignment:', foreground=text_color, font=('Ariel', 10))
alignment_label.place(x=348.5, y=250)
alignment_entry = ttk.Entry(root, textvariable=Alignment)
alignment_entry.place(x=348.5, y=270, width=89.5)


# margin left label and entry

marginl_label = ttk.Label(root, text='MarginL:', foreground=text_color, font=('Ariel', 10))
marginl_label.place(x=20, y=300)
marginl_entry = ttk.Entry(root, textvariable=MarginL)
marginl_entry.place(x=20, y=320, width=89.5)


# margin right label and entry

marginr_label = ttk.Label(root, text='MarginR:', foreground=text_color, font=('Ariel', 10))
marginr_label.place(x=129.5, y=300)
marginr_entry = ttk.Entry(root, textvariable=MarginR)
marginr_entry.place(x=129.5, y=320, width=89.5)


# margin vector label and entry

marginv_label = ttk.Label(root, text='MarginV:', foreground=text_color, font=('Ariel', 10))
marginv_label.place(x=239, y=300)
marginv_entry = ttk.Entry(root, textvariable=MarginV)
marginv_entry.place(x=239, y=320, width=89.5)


# Encoding label and entry

encoding_label = ttk.Label(root, text='Encoding:', foreground=text_color, font=('Ariel', 10))
encoding_label.place(x=348, y=300)
encoding_entry = ttk.Entry(root, textvariable=Encoding)
encoding_entry.place(x=348, y=320, width=89.5)

entry_list = [name_entry, fontname_entry, fontsize_entry, primarycolor_entry, secondarycolor_entry, outlinecolor_entry,
              backcolor_entry, bold_entry, italic_entry, underline_entry, strikeout_entry, scalex_entry, scaley_entry,
              spacing_entry, angel_entry, borderstyle_entry, outline_entry, shadow_entry, alignment_entry,
              marginl_entry, marginr_entry, marginv_entry, encoding_entry]
# set as default checkbox

setdefault_checkbox = tk.Checkbutton(root, text='Set setting as Default', fg=text_color, font=('Ariel', 10),
                                     variable=setasdefault)
setdefault_checkbox.place(x=20, y=350)


# clear all fields button

clearsetting_btn = tk.Button(root, text='Clear all fields', foreground='red', font=('Ariel', 11, 'bold'),
                             command=lambda: clear_fields(entry_list))
clearsetting_btn.place(x=323, y=350)


# load defaults button

btn_state = check_json()
loaddefaults_btn = tk.Button(root, text='Load Defaults', foreground=text_color, font=('Ariel', 11, 'bold'),
                             state=btn_state)
loaddefaults_btn.place(x=190, y=350)


# line seperator

seperator = ttk.Separator(root, orient='horizontal')
seperator.place(x=20, y=390, width=418)


# text area

fileslist_label = ttk.Label(root, text='Selected files:', foreground=text_color, font=('Ariel', 11, 'bold'))
fileslist_label.place(x=240, y=400)
files_listbox = tk.Listbox(root)
files_listbox.place(x=150, y=420, width=288, height=170)


# choose files button

choosefiles_button = tk.Button(root, text='Choose Files', foreground=text_color, font=('Ariel', 12, 'bold'),\
                               command=lambda: choose_files())
choosefiles_button.place(x=20, y=400, width=120)


# clear files button

clearfiles_btn = tk.Button(root, text='Clear Selected', foreground=text_color, font=('Ariel', 12, 'bold'),\
                           command=lambda : clear_selected())
clearfiles_btn.place(x=20, y=450, width=120)


# submit changes to files button

submit_btn = tk.Button(root, text='Submit', foreground=text_color, font=('Ariel', 12, 'bold'),
                       command=lambda: submit(setasdefault))
submit_btn.place(x=20, y=500, width=120)

# line seperator

seperator = ttk.Separator(root, orient='horizontal')
seperator.place(x=20, y=540, width=120)


# exit button

exit_btn = tk.Button(root, text='Exit', foreground=text_color, font=('Ariel', 12, 'bold'), command=root.quit)
exit_btn.place(x=20, y=550, width=120)





root.mainloop()

