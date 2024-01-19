import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter import messagebox
from ctypes import windll
import os
import json
import chardet

windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'


def choose_files():
    filetypes = (('.ass files', '*.ass'), ('.srt files', '*.srt'), ('All files', '*.*'))
    files = fd.askopenfilenames(parent=root, title='Choose files', filetypes=filetypes)
    #messagebox.askquestion(title='Selected files', message='Do you wish to continue?')
    i = 1
    for file in files:
        files_listbox.insert(i, file)
        i += 1


def menu_about():
    messagebox.showinfo(title='About', message='Replace .ass ver. 1.1.0\nBy David Hay Racha')


def clear_fields(entry_list):
    for entry in entry_list:
        entry.delete(0, 'end')
    setdefault_checkbox.deselect()
    srt2ass_checkbox.deselect()
    name_entry.focus()


def clear_selected():
    files_listbox.delete(0, 'end')


def checkbox_check(chk_var):
    if chk_var.get() == 1:
        return True
    return False

def check_fields(var_list, default_vars):
    i = 0
    for entry in entry_list:
        if len(entry.get()) == 0:
            x = len(entry.get())
            entry.insert(0, default_vars[i])
            y = entry.get()
        i += 1

'''i = 0
    for entry in entry_list:
        con = config.get(var_list[i])
        con = con.lstrip('&H')
        entry.insert(0, con)
        i += 1'''


def submit(chk_var, convert_box):
    check_fields(var_list, default_vars)
    chk_box_result = checkbox_check(chk_var)
    if chk_box_result:
        create_json(var_list, entry_list)
    convert_box = checkbox_check(convert_box)
    if convert_box:
        srt_list = []
        for i in range(files_listbox.size()):
            srt_list.append(files_listbox.get(i))
        new_files_name = srt_files(srt_list)
        listbox_new_files(new_files_name)
    change_files(entry_list)

    ## for checking ## print(chk_box_result)


def listbox_new_files(new_files_name):
    i = 0
    for new_file in new_files_name:
        files_listbox.insert(i, new_file)
        i += 1

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
                if entry == primarycolor_entry or entry == secondarycolor_entry or entry == outlinecolor_entry or entry == backcolor_entry:
                    con = reverse_entry(entry.get())
                else:
                    con = entry.get()
                json_dict[var_list[i]] = con
                i += 1
            js_object = json.dumps(json_dict, indent=4)
            with open('defaults.json', 'w') as f:
                f.write(js_object)
        else:
            return


def check_encoding(file):
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']


def open_file(file_path, ass_string):
    file_encoding = check_encoding(file_path)
    with open(file_path, 'r', encoding=str(file_encoding)) as asf:
        content = asf.readlines()
    i = 0
    for con in content:
        if con.startswith('Style'):
            content[i] = ass_string
            with open(file_path, 'w') as cf:
                cf.writelines(content)
        i += 1


def change_files(entry_list):
    ass_format = ''
    for entry in entry_list:
        if entry == primarycolor_entry or entry == secondarycolor_entry or entry == outlinecolor_entry or entry == backcolor_entry:
            con = reverse_entry(entry.get())
            ass_format += con + ','
        else:
            ass_format += (entry.get() + ',')
    ass_format = 'Style: ' + ass_format
    ass_format = ass_format.rstrip(ass_format[-1])
    ass_format = ass_format + '\n'
    file_num = files_listbox.size()
    for i in range(file_num):
        open_file(files_listbox.get(i), ass_format)

    clear_fields(entry_list)
    clear_selected()
        ## test ## print(files_listbox.get(i))


def reverse_entry(content):
    con = "".join(reversed([content[i:i + 2] for i in range(0, len(content), 2)]))
    return '&H' + con


def messages(msg):
    if msg == 1:
        messagebox.showinfo(title='Style name', message='The name of the Style. Case sensitive. Cannot include commas.')
    if msg == 2:
        messagebox.showinfo(title='Font name', message='The fontname as used by Windows. Case-sensitive.')
    if msg == 3:
        messagebox.showinfo(title='Font size', message='Literally what it says :-)')
    if msg == 4:
        messagebox.showinfo(title='Primary color', message='A long integer BGR (blue-green-red) value. ie. the byte order in the hexadecimal equivelent of this number is BBGGRR. This is the colour that a subtitle will normally appear in')
    if msg == 5:
        messagebox.showinfo(title='Secondary color', message=' A long integer BGR (blue-green-red)  value. ie. the byte order in the hexadecimal equivelent of this number is BBGGRR. This colour may be used instead of the Primary colour when a subtitle is automatically shifted to prevent an onscreen collsion, to distinguish the different subtitles.')
    if msg == 6:
        messagebox.showinfo(title='Outline color', message='A long integer BGR (blue-green-red)  value. ie. the byte order in the hexadecimal equivelent of this number is BBGGRR. This colour may be used instead of the Primary or Secondary colour when a subtitle is automatically shifted to prevent an onscreen collsion, to distinguish the different subtitles.')
    if msg == 7:
        messagebox.showinfo(title='Back color', message='This is the colour of the subtitle outline or shadow, if these are used. A long integer BGR (blue-green-red)  value. ie. the byte order in the hexadecimal equivelent of this number is BBGGRR')
    if msg == 8:
        messagebox.showinfo(title='Bold', message='This defines whether text is bold (true) or not (false). -1 is True, 0 is False. This is independant of the Italic attribute - you can have have text which is both bold and italic.')
    if msg == 9:
        messagebox.showinfo(title='Italic', message='This defines whether text is italic (true) or not (false). -1 is True, 0 is False. This is independant of the bold attribute - you can have have text which is both bold and italic.')
    if msg == 10:
        messagebox.showinfo(title='Underline', message='This defines whether text is underlined (true) or not (false). -1 is True, 0 is False. This is independant of the bold attribute - you can have have text which is both bold and italic.')
    if msg == 11:
        messagebox.showinfo(title='Strikeout', message='This defines whether text is striked-out (true) or not (false). -1 is True, 0 is False. This is independant of the bold attribute - you can have have text which is both bold and italic.')
    if msg == 12:
        messagebox.showinfo(title='ScaleX', message='Modifies the width of the font. [percent]')
    if msg == 13:
        messagebox.showinfo(title='ScaleY', message='Modifies the  height of the font. [percent]')
    if msg == 14:
        messagebox.showinfo(title='Spacing', message='Extra space between characters. [pixels]')
    if msg == 15:
        messagebox.showinfo(title='Angel', message='The origin of the rotation is defined by the alignment. Can be a floating point number. [degrees]')
    if msg == 16:
        messagebox.showinfo(title='Border style', message='1=Outline + drop shadow, 3=Opaque box')
    if msg == 17:
        messagebox.showinfo(title='Outline', message='If BorderStyle is 1,  then this specifies the width of the outline around the text, in pixels. Values may be 0, 1, 2, 3 or 4.')
    if msg == 18:
        messagebox.showinfo(title='Shadow', message='If BorderStyle is 1,  then this specifies the depth of the drop shadow behind the text, in pixels. Values may be 0, 1, 2, 3 or 4. Drop shadow is always used in addition to an outline - SSA will force an outline of 1 pixel if no outline width is given.')
    if msg == 19:
        messagebox.showinfo(title='Alignment', message='This sets how text is "justified" within the Left/Right onscreen margins, and also the vertical placing. Values may be 1=Left, 2=Centered, 3=Right. Add 4 to the value for a "Toptitle". Add 8 to the value for a "Midtitle". eg. 5 = left-justified toptitle. but after the layout of the numpad (1-3 sub, 4-6 mid, 7-9 top).')
    if msg == 20:
        messagebox.showinfo(title='MarginL', message='This defines the Left Margin in pixels. It is the distance from the left-hand edge of the screen.The three onscreen margins (MarginL, MarginR, MarginV) define areas in which the subtitle text will be displayed.')
    if msg == 21:
        messagebox.showinfo(title='MarginR', message='This defines the Right Margin in pixels. It is the distance from the right-hand edge of the screen. The three onscreen margins (MarginL, MarginR, MarginV) define areas in which the subtitle text will be displayed.')
    if msg == 22:
        messagebox.showinfo(title='MarginV', message='This defines the vertical Left Margin in pixels. For a subtitle, it is the distance from the bottom of the screen. For a toptitle, it is the distance from the top of the screen. For a midtitle, the value is ignored - the text will be vertically centred')
    if msg == 23:
        messagebox.showinfo(title='Encoding', message='This specifies the font character set or encoding and on multi-lingual Windows installations it provides access to characters used in multiple than one languages. It is usually 0 (zero) for English (Western, ANSI) Windows. When the file is Unicode, this field is useful during file format conversions.')


#def trim_left(content):
#    return content.strip('&H')


def load_defaults():
    with open('defaults.json', 'r') as f:
        config = json.load(f)
    i = 0
    for entry in entry_list:
        con = config.get(var_list[i])
        con = con.lstrip('&H')
        entry.insert(0, con)
        i += 1


def trimlinenum(line):
    line.pop(0)
    #print(line)
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


def check_utf():
    pass


def change_file_name(filename):
    return filename.replace('srt', 'ass')


def srt_files(files):
    hardcoded = ['[Script Info]', 'ScriptType: v4.00+', 'Collisions: Normal', 'PlayResX: 384', 'PlayResY: 288',
                 'Timer: 100.0000', '\n\n', '[V4+ Styles]', 'Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding',
                 'Style: Default,Tahoma,24,&H00ECEB50,&H00FFFFFF,&H00FFFFFF,&H00C0C0C0,-1,0,0,0,100,100,0,0.00,1,2,3,2,20,20,20,1',
                 '\n\n', '[Events]', 'Format: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text']
    #filetypes = ('All files', '*.*')
    #files = fd.askopenfilenames(parent=root, title='Choose files')#, filetypes=filetypes)
    #messagebox.askquestion(title='Selected files', message='Do you wish to continue?')
    file = ''

    sub_first = 'Dialogue: 0'
    asssublines = []
    new_file_list = []
    for file in files:
        subline = []
        sublines = []
        #file += item
        new_file = change_file_name(file)
        new_file_list.append(new_file)
        file_encoding = check_encoding(file)
        with open(file, 'r', encoding=file_encoding) as f:
            con = f.readlines()
        '''if con[len(con) - 1] == '\n':
            con = con[:-1]'''
        while con[len(con) - 1] == '\n':
            con = con[:-1]
        for item in con:
            if item != '\n':
                subline.append(item)
            else:
                sublines.append(subline)
                subline = []
        sublines.append(subline)

        #print(sublines)
    #asssub = ''

    #sub_Stime = ''
    #sub_Etime = ''
    #sub_text = ''

        for line in sublines:
            #print(line)
            asssub = ''
            line = trimlinenum(line)
            sub_start, sub_end = timeline(line[0])
            sub_text = get_text(line[1:len(line)])
            asssub = f'{sub_first},{sub_start},{sub_end},Default,,0000,0000,0000,,{sub_text}'
            asssublines.append(asssub)

        #sublines = []
    #print(asssub)
        #print(asssublines)

        with open(new_file, 'w', encoding='utf-8') as f:
            for item in hardcoded:
                f.write('%s\n' % item)

        with open(new_file, 'a', encoding='utf-8') as f:
            for assline in asssublines:
                f.write('%s\n' % assline)
        asssublines = []
    return new_file_list





# Create the main window

root = tk.Tk()
root.title('Subtitler')
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
srt2ass = tk.IntVar()
default_vars = ['Default', 'Tahoma', '24', 'FFFFFF', 'FFFFFF', 'FFFFFF', 'C0C0C0', '-1', '0', '0', '0', '100', '100',
                '0', '0.00', '1', '2', '3', '2', '20', '20', '20', '1']

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
file_menu.add_command(label='Submit')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)


# Create Edit Menu

edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Reset to Original')
edit_menu.add_command(label='Clear fields', command=lambda: clear_fields(entry_list))
edit_menu.add_command(label='Clear files', command=lambda : clear_selected())

# Create Help Menu

help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=menu_about)

# main window label

main_label = ttk.Label(root, text='Change .ass subtitle style', foreground=text_color, font=('Ariel', 14, 'bold'))
main_label.place(x=100, y=10)


# name label and entry

name_label = ttk.Label(root, text='Name:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
name_label.place(x=20, y=50)
name_label.bind('<Button-1>', lambda e: messages(1))
name_entry = tk.Entry(root, textvariable=Name)
name_entry.place(x=20, y=70)
name_entry.focus()


# font name label and entry

fontname_label = ttk.Label(root, text='Font Name:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
fontname_label.place(x=166, y=50)
fontname_label.bind('<Button-1>', lambda e: messages(2))
fontname_entry = tk.Entry(root, textvariable=Fontname)
fontname_entry.place(x=166, y=70)


# font size label and entry

fontsize_label = ttk.Label(root, text='Font Size:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
fontsize_label.place(x=312, y=50)
fontsize_label.bind('<Button-1>', lambda e: messages(3))
fontsize_entry = tk.Entry(root, textvariable=Fontsize)
fontsize_entry.place(x=312, y=70)#, width=61)


# primary color label and entry

primarycolor_label = ttk.Label(root, text='Primary Color:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
primarycolor_label.place(x=20, y=100)
primarycolor_label.bind('<Button-1>', lambda e: messages(4))
primarycolor_entry = tk.Entry(root, textvariable=PrimaryColour)
primarycolor_entry.place(x=20, y=120, width=89.5)


# secondary color label and entry

secondarycolor_label = ttk.Label(root, text='Secondary Color:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
secondarycolor_label.place(x=129.5, y=100)
secondarycolor_label.bind('<Button-1>', lambda e:messages(5))
secondarycolor_entry = tk.Entry(root, textvariable=SecondaryColour)
secondarycolor_entry.place(x=129.5, y=120, width=89.5)


# outline color label and entry

outlinecolor_label = ttk.Label(root, text='Outline Color:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
outlinecolor_label.place(x=239, y=100)
outlinecolor_label.bind('<Button-1>', lambda e:messages(6))
outlinecolor_entry = tk.Entry(root, textvariable=OutlineColour)
outlinecolor_entry.place(x=239, y=120, width=89.5)


# back coloe label and entry

backcolor_label = ttk.Label(root, text='Back Color:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
backcolor_label.place(x=348.5, y=100)
backcolor_label.bind('<Button-1>', lambda e:messages(7))
backcolor_entry = tk.Entry(root, textvariable=BackColour)
backcolor_entry.place(x=348.5, y=120, width=89.5)


# bold label and entry

bold_label = ttk.Label(root, text='Bold:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
bold_label.place(x=20, y=150)
bold_label.bind('<Button-1>', lambda e:messages(8))
bold_entry = tk.Entry(root, textvariable=Bold)
bold_entry.place(x=20, y=170, width=89.5)


# italic label and entry

italic_label = ttk.Label(root, text='Italic:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
italic_label.place(x=129.5, y=150)
italic_label.bind('<Button-1>', lambda e:messages(9))
italic_entry = tk.Entry(root, textvariable=Italic)
italic_entry.place(x=129.5, y=170, width=89.5)


# under line label and entry

underline_label = ttk.Label(root, text='Underline:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
underline_label.place(x=239, y=150)
underline_label.bind('<Button-1>', lambda e:messages(10))
underline_entry = tk.Entry(root, textvariable=Underline)
underline_entry.place(x=239, y=170, width=89.5)


# strikeout label and entry

strikeout_label = ttk.Label(root, text='Strikeout:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
strikeout_label.place(x=348.5, y=150)
strikeout_label.bind('<Button-1>', lambda e:messages(11))
strikeout_entry = tk.Entry(root, textvariable=StrikeOut)
strikeout_entry.place(x=348.5, y=170, width=89.5)


# scaleX label and entry

scalex_label = ttk.Label(root, text='ScaleX:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
scalex_label.place(x=20, y=200)
scalex_label.bind('<Button-1>', lambda e:messages(12))
scalex_entry = tk.Entry(root, textvariable=ScaleX)
scalex_entry.place(x=20, y=220, width=89.5)


# scaleY label and entry

scaley_label = ttk.Label(root, text='ScaleY:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
scaley_label.place(x=129.5, y=200)
scaley_label.bind('<Button-1>', lambda e:messages(13))
scaley_entry = tk.Entry(root, textvariable=ScaleY)
scaley_entry.place(x=129.5, y=220, width=89.5)


# spacing label and entry

spacing_label = ttk.Label(root, text='Spacing:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
spacing_label.place(x=239, y=200)
spacing_label.bind('<Button-1>', lambda e:messages(14))
spacing_entry = tk.Entry(root, textvariable=Spacing)
spacing_entry.place(x=239, y=220, width=89.5)


# angel label and entry

angel_label = ttk.Label(root, text='Angel:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
angel_label.place(x=348.5, y=200)
angel_label.bind('<Button-1>', lambda e:messages(15))
angel_entry = tk.Entry(root, textvariable=Angle)
angel_entry.place(x=348.5, y=220, width=89.5)


# border style label and entry

borderstyle_label = ttk.Label(root, text='Border Style:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
borderstyle_label.place(x=20, y=250)
borderstyle_label.bind('<Button-1>', lambda e:messages(16))
borderstyle_entry = tk.Entry(root, textvariable=BorderStyle)
borderstyle_entry.place(x=20, y=270, width=89.5)


# outline label and entry

outline_label = ttk.Label(root, text='Outline:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
outline_label.place(x=129.5, y=250)
outline_label.bind('<Button-1>', lambda e:messages(17))
outline_entry = tk.Entry(root, textvariable=Outline)
outline_entry.place(x=129.5, y=270, width=89.5)


# shadow label and entry

shadow_label = ttk.Label(root, text='Shadow:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
shadow_label.place(x=239, y=250)
shadow_label.bind('<Button-1>', lambda e:messages(18))
shadow_entry = tk.Entry(root, textvariable=Shadow)
shadow_entry.place(x=239, y=270, width=89.5)


# alignment label and entry

alignment_label = ttk.Label(root, text='Alignment:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
alignment_label.place(x=348.5, y=250)
alignment_label.bind('<Button-1>', lambda e:messages(19))
alignment_entry = tk.Entry(root, textvariable=Alignment)
alignment_entry.place(x=348.5, y=270, width=89.5)


# margin left label and entry

marginl_label = ttk.Label(root, text='MarginL:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
marginl_label.place(x=20, y=300)
marginl_label.bind('<Button-1>', lambda e:messages(20))
marginl_entry = tk.Entry(root, textvariable=MarginL)
marginl_entry.place(x=20, y=320, width=89.5)


# margin right label and entry

marginr_label = ttk.Label(root, text='MarginR:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
marginr_label.place(x=129.5, y=300)
marginr_label.bind('<Button-1>', lambda e:messages(21))
marginr_entry = tk.Entry(root, textvariable=MarginR)
marginr_entry.place(x=129.5, y=320, width=89.5)


# margin vector label and entry

marginv_label = ttk.Label(root, text='MarginV:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
marginv_label.place(x=239, y=300)
marginv_label.bind('<Button-1>', lambda e:messages(22))
marginv_entry = tk.Entry(root, textvariable=MarginV)
marginv_entry.place(x=239, y=320, width=89.5)


# Encoding label and entry

encoding_label = ttk.Label(root, text='Encoding:', foreground=text_color, font=('Ariel', 10), cursor='hand2')
encoding_label.place(x=348, y=300)
encoding_label.bind('<Button-1>', lambda e:messages(23))
encoding_entry = tk.Entry(root, textvariable=Encoding)
encoding_entry.place(x=348, y=320, width=89.5)

entry_list = [name_entry, fontname_entry, fontsize_entry, primarycolor_entry, secondarycolor_entry, outlinecolor_entry,
              backcolor_entry, bold_entry, italic_entry, underline_entry, strikeout_entry, scalex_entry, scaley_entry,
              spacing_entry, angel_entry, borderstyle_entry, outline_entry, shadow_entry, alignment_entry,
              marginl_entry, marginr_entry, marginv_entry, encoding_entry]


# set as default checkbox

setdefault_checkbox = tk.Checkbutton(root, text='Set setting as Default', fg=text_color, font=('Ariel', 10),
                                     variable=setasdefault)
setdefault_checkbox.place(x=20, y=345)


# Convert from .srt to .ass checkbox

srt2ass_checkbox = tk.Checkbutton(root, text='Convert .srt file to .ass', fg=text_color, font=('Ariel', 10), variable=srt2ass)
srt2ass_checkbox.place(x=20, y=370)


# clear all fields button

clearsetting_btn = tk.Button(root, text='Clear all fields', foreground='red', font=('Ariel', 11, 'bold'),
                             command=lambda: clear_fields(entry_list))
clearsetting_btn.place(x=323, y=350)


# load defaults button

btn_state = check_json()
loaddefaults_btn = tk.Button(root, text='Load Defaults', foreground=text_color, font=('Ariel', 11, 'bold'),
                             state=btn_state, command=lambda: load_defaults())
loaddefaults_btn.place(x=190, y=350)


# line seperator

seperator = ttk.Separator(root, orient='horizontal')
seperator.place(x=20, y=395, width=418)


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
                           command=lambda: clear_selected())
clearfiles_btn.place(x=20, y=450, width=120)


# submit changes to files button

submit_btn = tk.Button(root, text='Submit', foreground=text_color, font=('Ariel', 12, 'bold'),
                       command=lambda: submit(setasdefault, srt2ass))
submit_btn.place(x=20, y=500, width=120)

# line seperator

seperator = ttk.Separator(root, orient='horizontal')
seperator.place(x=20, y=540, width=120)



# exit button

exit_btn = tk.Button(root, text='Exit', foreground=text_color, font=('Ariel', 12, 'bold'), command=root.quit)
exit_btn.place(x=20, y=550, width=120)


root.mainloop()

