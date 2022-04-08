#
import tkinter

# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

# Open window having dimension 200x200
root.geometry('200x200')

# Create a Button
btn = Button(root, text = 'Click it!', bd = '5', command = root.destroy)

# Set the position of button on the top of the window
btn.pack(side = 'top')

root.mainloop()