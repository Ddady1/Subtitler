import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
from tkinter import messagebox
import os
import json
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
text_color = 'DodgerBlue4'

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
    subline = []
    sublines = []
    sub_first = 'Dialogue: 0'
    asssublines = []
    for file in files:
        #file += item
        new_file = change_file_name(file)
        with open(file, 'r', encoding='utf-8') as f:
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
            line = trimlinenum(line)
            sub_start, sub_end = timeline(line[0])
            sub_text = get_text(line[1:len(line)])
            asssub = f'{sub_first},{sub_start},{sub_end},Default,,0000,0000,0000,,{sub_text}'
            asssublines.append(asssub)
            #asssub = []
        sublines = []
    #print(asssub)
        #print(asssublines)

        with open(new_file, 'w', encoding='utf-8') as f:
            for item in hardcoded:
                f.write('%s\n' % item)

        with open(new_file, 'a', encoding='utf-8') as f:
            for assline in asssublines:
                f.write('%s\n' % assline)
        asssublines = []
    return new_file


    #print(lines)
    #i = 1
    #for line in lines:
    #    files_listbox.insert(i, line)
    #    i += 1



'''root = tk.Tk()
root.title('Set .ass Subtitle')
root.geometry('458x600+350+150')

choosefiles_button = tk.Button(root, text='Choose Files', foreground=text_color, font=('Ariel', 12, 'bold'),\
                               command=lambda: srt_files())
choosefiles_button.place(x=20, y=400, width=120)

exit_btn = tk.Button(root, text='Exit', command=root.quit)
exit_btn.place(x=20, y=500, width=120)


fileslist_label = ttk.Label(root, text='Selected files:', foreground=text_color, font=('Ariel', 11, 'bold'))
fileslist_label.place(x=240, y=400)
files_listbox = tk.Listbox(root)
files_listbox.place(x=150, y=420, width=288, height=170)


root.mainloop()'''
