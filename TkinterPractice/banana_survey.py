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

name_var = tk.StringVar(root)
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var) # input box

"""Entry widget is simple text-input box... Next is checkbutton"""
eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(
	root,
	text='Check this box if you eat bananas'
)

num_var = tk.IntVar(value=3)
num_label = tk.Label(
	root,
	text='How many bananas do you eat per day?'
)
num_inp = tk.Spinbox(root, from_=0, to=1000, increment=1)

# create simple 'listbox'
color_var = tk.StringVar(value='Any')
color_label = tk.Label(
	root,
	text='What is the best color for a banana?'
)
color_inp = tk.Listbox(root, height=1) # only show selected items
# add choices
color_choices = (
	'Any', 'Green', 'Green-Yellow', 'Yellow', 'Brown Spotted', 'Black'
)
color_inp = tk.OptionMenu(
	root, color_var, *color_choices
)
for choice in color_choices:
	color_inp.insert(tk.END, choice)


plantain_var = tk.BooleanVar()
plantain_label = tk.Label(root, text='Do you eat plantains?')
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes', value=True, variable=plantain_var)
plantain_no_inp = tk.Radiobutton(plantain_frame, text='Ewwwwwww, that\'s gross!', value=False, variable=plantain_var)

banana_haiku_label = tk.Label(
	root,
	text='Write a haiku about bananas'
)
banana_haiku_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text='Submit Survey')

output_line = tk.Label(root, text='', anchor='w', justify='left')

title.grid()

name_label.grid(row=1, column=0)

name_inp.grid(row=1, column=1)

title.grid(columnspan=2)

eater_inp.grid(row=1, column=1)

title.grid(columnspan=2)

eater_inp.grid(row=2, columnspan=2, sticky='we')

# something something
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))

color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

# plantain_var = tk.BooleanVar()
plantain_yes_inp.pack(sid='left', fill='x', ipadx=10, ipady=5)
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, stick=tk.W)


banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

root.columnconfigure(1, weight=1)

root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

"""Making the form DO something"""
# submit_btn.configure(command=on_submit)

def on_submit():
	"""To be run when the user submits the form"""
	name = name_inp.get()
	number = num_inp.get()

	selected_idx = color_inp.curselection()
	if selected_idx:
		color = color_inp.get(selected_idx)
	else:
		color = ''
	haiku = banana_haiku_inp.get('1.0', tk.END)

	message = (
		f'Thanks for taking the survey, {name}.\n'
		f'Enjoy your {number} {color} bananas!'
	)
	output_line.configure(text=message)
	print(haiku)

submit_btn.configure(command=on_submit)



"""to make the script runnable, type in root.mainloop()"""
root.mainloop()