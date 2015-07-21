#!/usr/bin/python3


from tkinter import *
from tkinter import ttk        
    
root = Tk()

label = ttk.Label(root, text = "MediaLab, Laboratorio de Arte, Diseño y Tecnología")
label.pack()
label.config(wraplength = 150)
label.config(justify = LEFT)
label.config(foreground = '#61888C', background = '#61888C')
label.config(font = ('Courier', 18, 'bold'))


logo = PhotoImage(file = 'image2502.gif') # change path to image as necessary
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')

label.img = logo
label.config(image = label.img)

root.mainloop()
