import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        #create the application variable
        self.contents = tk.StringVar()
        # Set it to some value
        self.contents.set("it can be whatever i make it")
        # Tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>',
                            self.print_contents)
    def print_contents(self, event):
        print("Hi. The curent entry content is:",
            self.contents.get())
root = tk.Tk()
myapp = App(root)
myapp.mainloop()