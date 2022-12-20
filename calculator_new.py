from tkinter import *
from tkinter import ttk


class CalculatorProject:

    def __init__(self):
        root = Tk()
        window1 = ttk.Frame(root, padding=0, borderwidth=1, relief="solid")
        display_text = ttk.Label(window1, borderwidth=5, relief="ridge", background="#D4CCBD", width=50)
        window2 = ttk.Frame(root, padding=10, borderwidth=3, relief="solid")
        button_seven = ttk.Button(window2, text="7")
        button_eight = ttk.Button(window2, text="8")
        button_nine = ttk.Button(window2, text="9")
        button_four = ttk.Button(window2, text="4")
        button_five = ttk.Button(window2, text="5")
        button_six = ttk.Button(window2, text="6")
        button_one = ttk.Button(window2, text="1")
        button_two = ttk.Button(window2, text="2")
        button_three = ttk.Button(window2, text="3")
        button_dot = ttk.Button(window2, text=".")
        button_zero = ttk.Button(window2, text="0")
        button_equals = ttk.Button(window2, text="=")
        button_division = ttk.Button(window2, text="/")
        button_multiplication = ttk.Button(window2, text="x")
        button_subtraction = ttk.Button(window2, text="-")
        button_addition = ttk.Button(window2, text="+")

        window1.grid(row=0, column=0)
        display_text.grid(row=0, column=0, ipady=8)
        window2.grid()
        button_seven.grid(row=1, column=0, ipadx=0, ipady=8)
        button_eight.grid(row=1, column=1, ipadx=0, ipady=8)
        button_nine.grid(row=1, column=2, ipadx=0, ipady=8)
        button_four.grid(row=2, column=0, ipadx=0, ipady=8)
        button_five.grid(row=2, column=1, ipadx=0, ipady=8)
        button_six.grid(row=2, column=2, ipadx=0, ipady=8)
        button_one.grid(row=3, column=0, ipadx=0, ipady=8)
        button_two.grid(row=3, column=1, ipadx=0, ipady=8)
        button_three.grid(row=3, column=2, ipadx=0, ipady=8)
        button_dot.grid(row=4, column=0, ipadx=0, ipady=8)
        button_zero.grid(row=4, column=1, ipadx=0, ipady=8)
        button_equals.grid(row=4, column=2, ipadx=0, ipady=8)
        button_division.grid(row=1, column=3, ipadx=0, ipady=8)
        button_multiplication.grid(row=2, column=3, ipadx=0, ipady=8)
        button_subtraction.grid(row=3, column=3, ipadx=0, ipady=8)
        button_addition.grid(row=4, column=3, ipadx=0, ipady=8)

        root.mainloop()


x = CalculatorProject()
