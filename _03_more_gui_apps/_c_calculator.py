"""
Create a simple calculator app
"""
import tkinter as tk

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label
class calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.multiplication = tk.Button(self, text="hi there!")
        self.addition = tk.Button()
        self.subtraction = tk.button()
        self.division = tk.button()
