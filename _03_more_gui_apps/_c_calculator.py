"""
Create a simple calculator app
"""
import tkinter as tk
from tkinter import messagebox, simpledialog

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.multiplication = tk.Button(self, text="*", fg='red',
                                        font=('courier new', 16, 'bold'), command=lambda : self.multiply_pressed())
        self.multiplication.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.2)
        self.addition = tk.Button(self, text="+", fg='red',
                                        font=('courier new', 16, 'bold'), command=lambda : self.addition_pressed())
        self.addition.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.2)
        self.subtraction = tk.Button(self, text="-", fg='red',
                                        font=('courier new', 16, 'bold'), command=lambda : self.subtraction_pressed())
        self.subtraction.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=0.2)
        self.division = tk.Button(self, text="/", fg='red',
                                        font=('courier new', 16, 'bold'), command=lambda : self.division_pressed())
        self.division.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.2)

    def multiply_pressed(self):
        self.multiplication.place()
        bee = simpledialog.askfloat(title='enter', prompt='enter the first number you wanna multiply')
        mult_2=simpledialog.askfloat(title='second number', prompt='')
        multiplication=bee*mult_2
        print(multiplication)
    def addition_pressed(self):
        self.addition.place()
        add_1=simpledialog.askfloat(title='kindly enter number',prompt='number 1')
        add_2=simpledialog.askfloat(title='kindly enter the second number',prompt='number 2')
        addition=add_1+add_2
        print(addition)
    def subtraction_pressed(self):
        self.subtraction.place()
        sub_1=simpledialog.askfloat(title='number 1',prompt='number 1')
        sub_2=simpledialog.askfloat(title='number 2',prompt='numer 2')
        subtraction=sub_1-sub_2
        print(subtraction)
    def division_pressed(self):
        self.division.place()
        div_1=simpledialog.askfloat(title='number 1',prompt='number 1')
        div_2=simpledialog.askfloat(title='number 2',prompt='number 2')
        division=div_1/div_2
        print(division)
if __name__=='__main__':
    math = Calculator()
    math.geometry('800x800')
    math.title('calc')
    math.mainloop()
