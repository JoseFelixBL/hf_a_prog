from tkinter import *


def tell_it():
    print("Hello, world!")


app = Tk()
app.title("Your TKInter app")
app.geometry('450x100+200+100')
b1 = Button(app, text="Click me!", width=10, command=tell_it)
b1.pack()


app.mainloop()
