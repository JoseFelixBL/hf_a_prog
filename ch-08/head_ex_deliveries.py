from tkinter import *
from pathlib import Path

app = Tk()
app.title("Head-Ex Deliveries")

Label(app, text="Depot:").pack()
depot = StringVar()
depot.set(None)
depots = ["Cambridge, MA", "Cambridge, UK", "Seattle, WA"]
OptionMenu(app, depot, *depots).pack()

Label(app, text="Description:").pack()

description = Entry(app)
description.pack()

Label(app, text="Address:").pack()

address = Text(app)
address.pack()


def save_data():
    dir = Path('ch-08')
    with open(dir / "deliveries.txt", "a") as file:
        file.write("Depot:\n")
        file.write(f"{depot.get()}\n")
        file.write("Description:\n")
        file.write(f"{description.get()}\n")
        file.write("Address:\n")
        file.write(f"{address.get('1.0', END)}\n")
        depot.set(None)
        description.delete(0, END)
        address.delete('1.0', END)


Button(app, text="Save", command=save_data).pack()

app.mainloop()
