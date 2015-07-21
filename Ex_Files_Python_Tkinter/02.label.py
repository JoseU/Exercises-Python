#!/usr/bin/python3
# notebook.py by Barron Stone

from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
label.config(text ="MediaLab, Laboratorio de Arte, Diseño y Tecnología")
label.config(foreground ='#61888C')
label.config(justify ='left')
label.config(font ='Courier')

img = "/Users/cottonmouth/Desktop/PYTHON\ PRUEBAS\ EA/Ex_Files_Python_Tkinter/image1909.png "
label = config(image = img)
