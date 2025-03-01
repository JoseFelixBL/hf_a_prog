from tkinter import *

number_correct = 0
number_wrong = 0


def play_correct_sound():
    global number_correct
    number_correct += 1


def play_wrong_sound():
    global number_wrong
    number_wrong += 1


app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

b1 = Button(app, text="Correct!", width=10, command=play_correct_sound)
b1.pack(side="left", padx=10, pady=10)

b2 = Button(app, text="Wrong!", width=10, command=play_wrong_sound)
b2.pack(side="right", padx=10, pady=10)


app.mainloop()

print(f"Number correct: {number_correct}")
print(f"Number wrong: {number_wrong}")
print(f'Total answers: {number_correct + number_wrong}')
