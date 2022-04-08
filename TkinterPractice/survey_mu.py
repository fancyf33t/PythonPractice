# banana survey
"""A banana survey written in Python using Tkinter"""

import tkinter as tk

# import tkinter
# from tkinter import *

root = tk.Tk()

# set the title
root.title('Banana interest survey')
# set the root window size
root.geometry('640x480+300+300')
root.resizable(False, False) # root.resizable allows you to set whether or not resizine is possible

title = tk.Label(
	root,
	text='Please take the survey',
	font=('Arial 16 bold'),
	bg='brown',
	fg='#FF0'
)

name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root) # input box

"""Entry widget is simple text-input box... Next is checkbutton"""
eater_inp = tk.Checkbutton(
	root,
	text='Check this box if you eat bananas'
)

num_label = tk.Label(
	root,
	text='How many bananas do you eat per day?'
)
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)

# create simple 'listbox'
color_label = tk.Label(
	root,
	text='What is the best color for a banana?'
)
color_inp = tk.Listbox(root, height=1) # only show selected items
# add choices
color_choices = (
	'Any', 'Green', 'Green-Yellow', 'Yellow', 'Brown Spotted', 'Black'
)
for choice in color_choices:
	color_inp.insert(tk.END, choice)
