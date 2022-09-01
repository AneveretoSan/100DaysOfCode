from tkinter import *
#from Button import Button

#class Window:

    #button = Button()

#def __init__(self):

def click():
    print("scissors")

window = Tk()
icon = PhotoImage(file = 'P:\\jinja\\Programación\\100DaysOfCodding\\Rock paper and scissors\\rock-paper-scissors.png')
scissors = PhotoImage(file = 'P:\\jinja\\Programación\\100DaysOfCodding\\Rock paper and scissors\\scissors.png')



window.geometry("900x700")
window.title("Rock, Paper and Scissors")
window.iconphoto(True, icon)
window.config(
    background="#ADE6FF",)

label = Label(
    window,
    text = "Rock Paper and Scissors",
    font = ('Cascadia Mono', 24, 'bold'),
    fg = '#FFFFFF',
    bg = '#0267BD',
    relief = RAISED,
    bd = 5,
    padx = 5,
    pady = 5)
label.pack()

button = Button(window, 
    command = click,
    bg  = '#FB7DD1',
    activebackground = '#FB7DD1',
    state = ACTIVE,
    image = scissors,
    compound = 'bottom',
)

button.pack()

window.mainloop()

