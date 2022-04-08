# information about ABQ:
# - ABQ facility has three greenhouses, each operating with a different climate, marked A, B, and C
# - each greenhouse has 20 plots (labeled 1 - 20)
# - each plot has 20 seeds of a given sample planted in it (plus sensor unit)


"""The ABQ Data Entry application"""

from ast import Return
import tkinter as tk 
from tkinter import ttk 
from datetime import datetime 
from pathlib import Path 
import csv 

# create global variables that the app will use to keep track of information
variables = dict()
records_saved = 0

# create and configure the root window
root = tk.Tk()
root.title('ABQ Data Entry Application')
root.columnconfigure(0, weight=1)

# add a heading for the application
ttk.Label(
    root, text="ABQ Data Entry Application",
    font=("TkDefaultFont", 16)
).grid()

"""BUILDING THE DATA RECORD FORM"""
# create a frame to contain the entire data record form, called drf
drf = ttk.Frame(root)
drf.grid(padx=0, sticky=(tk.E + tk.W))
drf.columnconfigure(0, weight=1)

"""RECORD INFORMATION SECTION"""
# create and configure a LabelFrame to store information
r_info = ttk.LabelFrame(drf, text='Record Information')
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)

# create the contents of the frame, starting with the first input widge, the Date field
variables['Date'] = tk.StringVar() # control variable
ttk.Label(r_info, text='Date').grid(row=0, column=0)
ttk.Entry(
    r_info, textvariable=variables['Date']
).grid(row=1, column=0, sticky=(tk.W + tk.E))

# add the Time and Technician fields
time_values = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = tk.StringVar()
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(
    r_info, textvariable=variables['Time'], values=time_values
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Technician'] = tk.StringVar()
ttk.Label(r_info, text='Technician').grid(row=0, column=2)
ttk.Entry(
    r_info, textvariable=variables['Technician']
).grid(row=1, column=2, sticky=(tk.W + tk.E))

# on the second row, start with Lab inputs
variables['Lab'] = tk.StringVar()
ttk.Label(r_info, text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
        labframe, value=lab, text=lab, variable=variables['Lab']
    ).pack(side=tk.LEFT, expand=True)
    labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))

# add remaining portion, the Plot and Seed Sample fields
variables['Plot'] = tk.IntVar()
ttk.Label(r_info, text='Plot').grid(row=2, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['Plot'],
    values=list(range(1, 21))
).grid(row=3, column=1, sticky=(tk.W + tk.E))

variables['Seed Sample'] = tk.StringVar()
ttk.Label(r_info, text='See Sample').grid(row=2, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['Seed Sample']
).grid(row=3, column=2, sticky=(tk.W + tk.E))

"""ENVIRONMENT DATA SECTION"""
# create the Environment Data frame
e_info = ttk.LabelFrame(drf, text="Environment Data")
e_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    e_info.columnconfigure(i, weight=1)

# populate with Humidity, Light, and Temperature widgets
variables['Humidity'] = tk.DoubleVar()
ttk.Label(e_info, text="Humidity (g/m3)").grid(row=0, column=0)
ttk.Spinbox(
    e_info, textvariable=variables['Humidity'],
    from_=0.5, to=52.0, increment=0.01,
).grid(row=1, column=0, sticky=(tk.W + tk.E))

variables['Light'] = tk.DoubleVar()
ttk.Label(e_info, text='Light (klx)').grid(row=0, column=1)
ttk.Spinbox(
    e_info, textvariable=variables['Light'],
    from_=0, to=100, increment=0.01
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Temperature'] = tk.DoubleVar()
ttk.Label(e_info, text='Temperature (C)').grid(row=0, column=2)
ttk.Spinbox(
    e_info, textvariable=variables['Temperature'],
    from_=4, to=40, increment=.01
).grid(row=1, column=2, sticky=(tk.W + tk.E))

# for the second row, add Equipment Fault check button
variables['Equipment Fault'] = tk.BooleanVar(value=False)
ttk.Checkbutton(
    e_info, variable=variables['Equipment Fault'],
    text='Equipment Fault'
).grid(row=2, column=0, sticky=tk.W, pady=5)

"""PLANT DATA SECTION"""
p_info = ttk.LabelFrame(drf, text="Plant Data")
p_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    p_info.columnconfigure(i, weight=1)

# add the first row of inputs, Plants, Blossoms, and Fruit
variables['Plants'] = tk.IntVar()
ttk.Label(p_info, text='Plants').grid(row=0, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Plants'],
    from_=0, to=20, increment=1
).grid(row=1, column=0, sticky=(tk.W + tk.E))

variables['Blossoms'] = tk.IntVar()
ttk.Label(p_info, text='Blossoms').grid(row=0, column=1)
ttk.Spinbox(
    p_info, textvariable=variables['Blossoms'],
    from_=0, to=1000, increment=1
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Fruit'] = tk.IntVar()
ttk.Label(p_info, text='Fruit').grid(row=0, column=2)
ttk.Spinbox(
    p_info, textvariable=variables['Fruit'],
    from_=0, to=1000, increment=1
).grid(row=1, column=2, sticky=(tk.W + tk.E))

# add last row of inputs, Min Height, Max Height, and Med Height
variables['Min Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Min Height (cm)').grid(row=2, column=0)
ttk.Spinbox(
    p_info, textvariable=variables['Min Height'],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=0, sticky=(tk.W + tk.E))

variables['Max Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Max Height (cm)').grid(row=2, column=1)
ttk.Spinbox(
    p_info, textvariable=variables['Max Height'],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=1, sticky=(tk.W + tk.E))

variables['Med Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Median Height (cm)').grid(row=2, column=2)
ttk.Spinbox(
    p_info, textvariable=variables['Med Height'],
    from_=0, to=1000, increment=0.01
).grid(row=3, column=2, sticky=(tk.W + tk.E))

"""FINISHING THE GUI"""
ttk.Label(drf, text="Notes").grid()
notes_inp = tk.Text(drf, width=75, height=10)
notes_inp.grid(sticky=(tk.W + tk.E))

# add buttons
buttons = tk.Frame(drf)
buttons.grid(sticky=tk.E + tk.W)
save_button = ttk.Button(buttons, text='Save')
save_button.pack(side=tk.RIGHT)

reset_button = ttk.Button(buttons, text='Reset')
reset_button.pack(side=tk.RIGHT)

# add a status bar
status_variable = tk.StringVar()
ttk.Label(
    root, textvariable=status_variable
).grid(sticky=tk.W + tk.E, row=99, padx=10)

# ####################################

def on_reset():
    """Called when reset button is clicked, or after save"""
    for variable in variables.values():
        if isinstance(variable, tk.BooleanVar):
            variable.set(False)
        else:
            variable.set('')

    notes_inp.delete('1.0', tk.END)

reset_button.configure(command=on_reset)

# #####################################

def on_save():
    """Handle save button clicks"""
    global records_saved

# #####################################
datestring = datetime.today().strftime("%Y-%m-%d")
filename = f"abq_data_record_{datestring}.csv"
newfile = not Path(filename).exists()


data = dict()
fault = variables['Equipment Fault'].get()
for key, variable in variables.items():
    if fault and key in ('Light', 'Humidity', 'Temperature'):
        data[key] = ''
    else:
        try:
            data[key] = variable.get()
        except tk.TclError:
            status_variable.set(
                f'Error in field: {key}. Data was not saved!'
            )
            Return
# get the Text widget contents separatesly
data['Notes'] = notes_inp.get('1.0',)

with open(filename, 'a', newline='') as fh:
    csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
    if newfile:
        csvwriter.writeheader()
    csvwriter.writerow(data)


# do i place this in the on_save() function??
records_saved += 1
status_variable.set(
    f"{records_saved} records saved this session"
)
on_reset()

# bind to button
save_button.configure(command=on_save)

# reset the form and launch the main event loop
on_reset()
root.mainloop()