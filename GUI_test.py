from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image


try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

def select():
    sf = "value is %s" % var.get()
    root.title(sf)
    # optional
    color = var.get()
    root['bg'] = color

    if color == 'green':
        canvas = Canvas(root, width = 1650, height = 800)  
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("images/Canada.png"))  
        canvas.create_image(0, 0, anchor=NW, image=img)

        root.mainloop()



root = tk.Tk()

# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (1400, 1000,30, 10))
root.title("tk.Optionmenu as combobox")

var = tk.StringVar(root)
# initial value
var.set('red')

choices = ['red', 'green', 'blue', 'yellow','white', 'magenta']
option = tk.OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)

button = tk.Button(root, text="check value slected", command=select)
button.pack(side='left', padx=20, pady=10)

if choices == 'green':
    print('hi')

root.mainloop()