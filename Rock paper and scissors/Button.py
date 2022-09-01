from tkinter import *
from Window import Window

window = Window()

icon = PhotoImage(file = 'P:\\jinja\\Programación\\100DaysOfCodding\\Rock paper and scissors\\Icons\\scissors.png')

def __init__(self):

    button = Button(window, 
        command = click,
        bg  = '#FB7DD1',
        activebackground = '#FB7DD1',
        state = ACTIVE,
        image = icon,
        compound = 'bottom'
    )

    button.pack()

def click():
    print("scissors")

