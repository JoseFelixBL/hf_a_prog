from tkinter import *

import pygame.mixer
from pathlib import Path


def play_correct_sound():
    num_good.set(num_good.get()+1)
    correct_s.play()


def play_wrong_sound():
    num_bad.set(num_bad.get()+1)
    wrong_s.play()


app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

sounds = pygame.mixer
sounds.init()

dir = Path('ch-07')
correct_s = sounds.Sound(dir / "correct.wav")
wrong_s = sounds.Sound(dir / "wrong.wav")

num_good = IntVar()
num_good.set(0)
num_bad = IntVar()
num_bad.set(0)

lab = Label(app, text='When you are ready, click on the buttons!', height=3)
lab.pack()

lab_g = Label(app, textvariable=num_good, height=3)
lab_g.pack(side="left")

lab_b = Label(app, textvariable=num_bad, height=3)
lab_b.pack(side="right")

b1 = Button(app, text="Correct!", width=10, command=play_correct_sound)
b1.pack(side="left", padx=10, pady=10)

b2 = Button(app, text="Wrong!", width=10, command=play_wrong_sound)
b2.pack(side="right", padx=10, pady=10)


app.mainloop()
