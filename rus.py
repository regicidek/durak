from tkinter import *
wind = Tk()
wind.geometry('250x250')



lbl = Label(wind, text="ты дурак?")
lbl.pack()

def btnclk1():
    labl = Label(wind, text="ты знаешь чей ответ.").place(x=70, y=55)




def btnclk():
    labl = Label(wind, text="                я знаю                      ").place(x=60, y=55)

btn1 = Button(wind, text="да", command=btnclk).place(x=90, y=25)
btn2 = Button(wind, text="нет", command=btnclk1).place(x=135, y=25)

mainloop()