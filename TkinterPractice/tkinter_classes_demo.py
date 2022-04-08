# import
import tkinter as tk 
import json 

# Begin the new variable class by creating a subclass of tk.StringVar
class JSONVar(tk.StringVar):
    """A Tk variable that can hold dicts and lists"""

    def __init__(self, *args, **kwargs):
        kwargs['value'] = json.dumps(kwargs.get('value'))
        super().__init__(*args, **kwargs)

    def set(self, value, *args, **kwargs):
        string = json.dumps(value)
        super().set(string, *args, **kwargs)

    def get(self, *args, **kwargs):
        string = super().get(*args, **kwargs)
        return json.loads(string)

# root = tk.Tk()
# var1 = JSONVar(root)
# var1.set([1, 2, 3])
# var2 = JSONVar(root, value={'a': 10, 'b': 15})


class LabelInput(tk.Frame):
    """A label and input combined together"""

    def __init__(
        self, parent, label, inp_cls,
        inp_args, *args, **kwargs
    ):
     super().__init__(parent, *args, **kwargs)

     self.label = tk.Label(self, text=label, anchor='w')
     self.input = inp_cls(self, **inp_args)

# li1 = LabelInput(root, 'Name', tk.Entry, {'bg': 'red'})
# li1.grid()

# age_var = tk.IntVar(root, value=21)
# li2 = LabelInput(
#     root, 'Age', tk.Spinbox,
#     {'textvariable': age_var, 'from_': 10, 'to': 150}
# )
# li2.grid()

# create a MyForm class to hold simple form information
class MyForm(tk.Frame):

    def __init__(self, parent, data_var, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data_var = data_var 

# create some internal control variables to bind to our form widgets
        self.vars = {
            'name': tk.StringVar(self),
            'age': tk.IntVar(self, value=2)
        }

# put LabelInput class to work to create the actual widgets for the form
        LabelInput(
            self, 'Name', tk.Entry,
            {'textvariable': self._vars['name']}
        ).grid(sticky=tk.E + tk.W)
        LabelInput(
            self, 'Age', tk.Spinbox,
            {'textvariable': self._vars['age'], 'from_': 10, 'to': 150}
        ).grid(sticky=tk.E + tk.W)

        tk.Button(self, text='Submit', command=self._on_submit).grid()
    
    def _on_submit(self):
        data = { key: var.get() for key, var in self._vars.items() }
        self.data_var.set(data)

"""SUBCLASSING TK"""
class Application(tk.Tk):
    """a simple form application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jsonvar = JSONVar(self)
        self.output_var = tk.StringVar(self)

        tk.Label(self, text='Please fill the form').grid(sticky='ew')
        MyForm(self, self.jsonvar).grid(sticky='nsew')
        tk.Label(self, textvariable=self.out_var).grid(sticky='ew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # since a submission of MyForm updates the JSONVar object we passed to it, we need to execute a submission-handling callback
        self.jsonvar.trace_add('write', self._on_data_change)
    
    def _on_data_change(self, *args, **kwargs):
        data = self.jsonvar.get()
        output = ''.join([
            f'{key} = {value}\n'
            for key, value in data.items()
        ])
        self.output_var.set(output)

if __name__ == "__main__":
    app = Application()
    app.mainloop()