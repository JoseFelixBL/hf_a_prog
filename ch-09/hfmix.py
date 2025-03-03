from tkinter import *
import pygame.mixer

app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')

mixer = pygame.mixer
mixer.init()

sound_file = "50459_M_RED_Nephlimizer.wav"
track = mixer.Sound(sound_file)


def track_start():
    track.play(loops=-1)


def track_stop():
    track.stop()


start_button = Button(app, command=track_start, text="Start")
start_button.pack(side=LEFT)

stop_button = Button(app, command=track_stop, text="Stop")
stop_button.pack(side=RIGHT)

app.mainloop()
