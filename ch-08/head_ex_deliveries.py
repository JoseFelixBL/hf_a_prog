from tkinter import *
from pathlib import Path


def save_data():
    dir = Path('ch-08')
    try:
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
    except Exception as ex:
        print(f"An error occurred: {ex}")


def read_depots(file):
    dir = Path('ch-08')
    depots = []
    with open(dir / file, "r") as file:
        for line in file:
            depots.append(line.strip())
    return depots


app = Tk()
app.title("Head-Ex Deliveries")

Label(app, text="Depot:").pack()
depot = StringVar()
depot.set(None)
depots = read_depots("depots.txt")
OptionMenu(app, depot, *depots).pack()

Label(app, text="Description:").pack()

description = Entry(app)
description.pack()

Label(app, text="Address:").pack()

address = Text(app)
address.pack()


Button(app, text="Save", command=save_data).pack()

app.mainloop()
