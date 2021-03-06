#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#    Feb 25, 2022 11:44:20 AM CET  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import filedialog
import gui_support
from gen_alphabet import generate_alphabet
from ciphers.vigener import VigenerCipher

class KPB:
    def __init__(self, top=None):
        self.alphabet = generate_alphabet(65, 90)
        self.specified_key = "ZIMA"
        self.v_c = VigenerCipher(self.alphabet)

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x441+521+307")
        top.minsize(120, 1)
        top.maxsize(3004, 1901)
        top.resizable(1,  1)
        top.title("KPB")
        top.configure(background="#72d56c")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Title = tk.Label(self.top)
        self.Title.place(relx=0.0, rely=0.0, height=31, width=614)
        self.Title.configure(activebackground="#f9f9f9")
        self.Title.configure(activeforeground="black")
        self.Title.configure(anchor='n')
        self.Title.configure(background="#8fe75a")
        self.Title.configure(compound='left')
        self.Title.configure(disabledforeground="#a3a3a3")
        self.Title.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Title.configure(foreground="#000000")
        self.Title.configure(highlightbackground="#d9d9d9")
        self.Title.configure(highlightcolor="black")
        self.Title.configure(text='''Kryptografie''')

        self.OAFrame = ttk.Frame(self.top)
        self.OAFrame.place(relx=0.017, rely=0.091, relheight=0.896
                , relwidth=0.442)
        self.OAFrame.configure(relief='groove')
        self.OAFrame.configure(borderwidth="2")
        self.OAFrame.configure(relief="groove")

        self.ToSA = tk.Button(self.OAFrame, command=self.handle_to_sa)
        self.ToSA.place(relx=0.0, rely=0.937, height=24, width=267)
        self.ToSA.configure(activebackground="#ececec")
        self.ToSA.configure(activeforeground="#000000")
        self.ToSA.configure(background="#d9d9d9")
        self.ToSA.configure(compound='left')
        self.ToSA.configure(disabledforeground="#a3a3a3")
        self.ToSA.configure(foreground="#000000")
        self.ToSA.configure(highlightbackground="#d9d9d9")
        self.ToSA.configure(highlightcolor="black")
        self.ToSA.configure(pady="0")
        self.ToSA.configure(text='''Na SA''')





        self.OAText = tk.Text(self.OAFrame)
        self.OAText.place(relx=0.038, rely=0.101, relheight=0.82, relwidth=0.921)

        self.OAText.configure(background="white")
        self.OAText.configure(font="TkTextFont")
        self.OAText.configure(foreground="black")
        self.OAText.configure(highlightbackground="#d9d9d9")
        self.OAText.configure(highlightcolor="black")
        self.OAText.configure(insertbackground="black")
        self.OAText.configure(selectbackground="blue")
        self.OAText.configure(selectforeground="white")
        self.OAText.configure(wrap="word")

        self.OAExport = tk.Button(self.OAFrame, command=self.create_export_to(self.OAText))
        self.OAExport.place(relx=0.528, rely=0.025, height=24, width=107)
        self.OAExport.configure(activebackground="#ececec")
        self.OAExport.configure(activeforeground="#000000")
        self.OAExport.configure(background="#d9d9d9")
        self.OAExport.configure(compound='left')
        self.OAExport.configure(disabledforeground="#a3a3a3")
        self.OAExport.configure(foreground="#000000")
        self.OAExport.configure(highlightbackground="#d9d9d9")
        self.OAExport.configure(highlightcolor="black")
        self.OAExport.configure(pady="0")
        self.OAExport.configure(text='''Export''')

        self.OAImport = tk.Button(self.OAFrame, command=self.create_import_to(self.OAText))
        self.OAImport.place(relx=0.075, rely=0.025, height=24, width=107)
        self.OAImport.configure(activebackground="#ececec")
        self.OAImport.configure(activeforeground="#000000")
        self.OAImport.configure(background="#d9d9d9")
        self.OAImport.configure(compound='left')
        self.OAImport.configure(disabledforeground="#a3a3a3")
        self.OAImport.configure(foreground="#000000")
        self.OAImport.configure(highlightbackground="#d9d9d9")
        self.OAImport.configure(highlightcolor="black")
        self.OAImport.configure(pady="0")
        self.OAImport.configure(text='''Import''')

        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(relx=0.533, rely=0.091, relheight=0.896
                , relwidth=0.442)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.ToOA = tk.Button(self.TFrame1, command=self.handle_to_oa)
        self.ToOA.place(relx=0.0, rely=0.937, height=24, width=267)
        self.ToOA.configure(activebackground="#ececec")
        self.ToOA.configure(activeforeground="#000000")
        self.ToOA.configure(background="#d9d9d9")
        self.ToOA.configure(compound='left')
        self.ToOA.configure(disabledforeground="#a3a3a3")
        self.ToOA.configure(foreground="#000000")
        self.ToOA.configure(highlightbackground="#d9d9d9")
        self.ToOA.configure(highlightcolor="black")
        self.ToOA.configure(pady="0")
        self.ToOA.configure(text='''Na OA''')

        self.SAText = tk.Text(self.TFrame1)
        self.SAText.place(relx=0.038, rely=0.101, relheight=0.82, relwidth=0.921)

        self.SAText.configure(background="white")
        self.SAText.configure(font="TkTextFont")
        self.SAText.configure(foreground="black")
        self.SAText.configure(highlightbackground="#d9d9d9")
        self.SAText.configure(highlightcolor="black")
        self.SAText.configure(insertbackground="black")
        self.SAText.configure(selectbackground="blue")
        self.SAText.configure(selectforeground="white")
        self.SAText.configure(wrap="word")

        self.SAImport = tk.Button(self.TFrame1, command=self.create_import_to(self.SAText))
        self.SAImport.place(relx=0.075, rely=0.025, height=24, width=107)
        self.SAImport.configure(activebackground="#ececec")
        self.SAImport.configure(activeforeground="#000000")
        self.SAImport.configure(background="#d9d9d9")
        self.SAImport.configure(compound='left')
        self.SAImport.configure(disabledforeground="#a3a3a3")
        self.SAImport.configure(foreground="#000000")
        self.SAImport.configure(highlightbackground="#d9d9d9")
        self.SAImport.configure(highlightcolor="black")
        self.SAImport.configure(pady="0")
        self.SAImport.configure(text='''Import''')

        self.SAExport = tk.Button(self.TFrame1, command=self.create_export_to(self.SAText))
        self.SAExport.place(relx=0.528, rely=0.025, height=24, width=107)
        self.SAExport.configure(activebackground="#ececec")
        self.SAExport.configure(activeforeground="#000000")
        self.SAExport.configure(background="#d9d9d9")
        self.SAExport.configure(compound='left')
        self.SAExport.configure(disabledforeground="#a3a3a3")
        self.SAExport.configure(foreground="#000000")
        self.SAExport.configure(highlightbackground="#d9d9d9")
        self.SAExport.configure(highlightcolor="black")
        self.SAExport.configure(pady="0")
        self.SAExport.configure(text='''Export''')

    def handle_to_oa(self):
        print("Handling OA")
        self.decode()
    
    def handle_to_sa(self):
        print("Handling SA")
        self.encode()

    def decode(self):
        sa_text = self.SAText.get("1.0", END)
        sa_text = sa_text.replace('\n', '')
        oa_text = self.v_c.decode(sa_text, self.specified_key)
        self.write_into(self.OAText, oa_text)

    def encode(self):
        oa_text = self.OAText.get("1.0", END)
        oa_text = oa_text.replace('\n', '')
        sa_text = self.v_c.encode(oa_text, self.specified_key)
        self.write_into(self.SAText, sa_text)

    def write_into(self, text_area, text):
        text_area.delete("1.0", END)
        text_area.insert(INSERT, text)

    def read_file(self, path):
        with open(path, 'r') as f:
            return f.read()

    def create_import_to(self, text_area):
        def handle_import():
            print('Handling import')
            path_to_file = filedialog.askopenfilename()
            content = self.read_file(path_to_file)
            self.write_into(text_area, content)
        return handle_import

    def create_export_to(self, text_area):
        def handle_export():
            print("Handling export")
            content = text_area.get("1.0", END)
            files = [
                ('All Files', '*.*'), 
                ('Python Files', '*.py'),
                ('Text Document', '*.txt')
            ]
            file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
            file.write(content)
            file.close()
        return handle_export

def start_up():
    gui_support.main()

if __name__ == '__main__':
    gui_support.main()




