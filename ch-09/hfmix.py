from tkinter import *
import pygame.mixer
from sound_panel import *
import os

app = Tk()
app.title("Head First Mix")

mixer = pygame.mixer
mixer.init()


def shutdown():
    # track.stop()  # No hace falta, app.destroy cierra todo.
    app.destroy()


dirList = os.listdir(".")
for fname in dirList:
    if fname.endswith(".wav"):
        panel = SoundPanel(app, mixer, fname)
        panel.pack()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
