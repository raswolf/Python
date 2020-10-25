"""
Program: gui_assignment.py
Author: Rachael Wolf
Last date modified: 10/24/2020

The purpose of this program is to create a checkbox gui window with a responsive message
"""

import tkinter


def pick_breakfast():
    label.config(text="Nice choice")


def pick_second_breakfast():
    label.config(text="Good one")


def pick_lunch():
    label.config(text="Don't forget")


def pick_dinner():
    label.config(text="Thank the cook")


m = tkinter.Tk()
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)
button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen
