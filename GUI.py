"""
Created on Wed Oct 11 00:29:21 2017

@author: hemanthkumar
"""

import pybrl as brl
import Tkinter
from Tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    example=brl.translate(e.get())
    #print(example)
    T.delete("1.0", Tkinter.END)
    T.insert(END,brl.toUnicodeSymbols(example, flatten=True))
    #print e.get()

b = Button(master, text="Convert to Braille", width=20, command=callback)
b.pack()
T = Text(master, height=10, width=30)
T.pack()

mainloop()
e = Entry(master, height = 10,width=1000)
e.pack()


text = e.get()
