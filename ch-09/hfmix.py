from tkinter import *
import pygame.mixer
from sound_panel import *

app = Tk()
app.title("Head First Mix")

mixer = pygame.mixer
mixer.init()


def shutdown():
    # track.stop()  # No hace falta, app.destroy cierra todo.
    app.destroy()


panel = SoundPanel(app, mixer, "50459_M_RED_Nephlimizer.wav")
panel.pack()
panel = SoundPanel(app, mixer, "49119_M_RED_HardBouncer.wav")
panel.pack()

app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
