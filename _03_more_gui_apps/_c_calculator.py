"""
Create a simple calculator app
"""
import tkinter as tk
from tkinter import messagebox, simpledialog

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label

class calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.multiplication = tk.Button(self, text="hi there!", fg='red',
                                        font=('courier new', 16, 'bold')command=self.multiply_pressed)
        self.multiplication.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
        self.addition = tk.Button(self, text="hi there!", fg='red',
                                        font=('courier new', 16, 'bold'))
        self.addition.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
        self.subtraction = tk.Button(self, text="hi there!", fg='red',
                                        font=('courier new', 16, 'bold'))
        self.subtraction.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)
        self.division = tk.Button(self, text="hi there!", fg='red',
                                        font=('courier new', 16, 'bold'), command=multiply_pressed)
        self.division.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)

        def multiply_pressed(self):
            self.multiplication.place()
            bee = simpledialog.askinterger('enter', 'enter the first number you wanna multiply')
            mult_2=simpledialog.askinteger('second number')
            multiplication=bee*mult_2
            print(multiplication)
        def addition_preessed(self):
            self.addition.place()
            add_1=simpledialog.askinteger('kindly enter number',)
            add_2=simpledialog.askinteger('kindly enter the second number',)
            addition=add_1+add_2
            print(addition)
        def subtraction_pressed(self):
            self.subtraction.place()
            sub_1=simpledialog.askinteger('number 1')
            sub_2=simpledialog.askinteger('number 2')
            subtraction=sub_1-sub_2
            print(subtraction)
        def division_pressed(self):
            self.division.place()
            div_1=simpledialog.askinteger('number 1')
            div_2=simpledialog.askinteger('number 2')
            division=div_1/div_2
            print(division)
if __name__=='__main__':
    math = calculator
    math.title('calc')
