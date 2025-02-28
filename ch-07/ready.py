import pygame.mixer
from pathlib import Path

sounds = pygame.mixer
sounds.init()


def wait_finish(channel):
    while channel.get_busy():
        pass


dir = Path('ch-07')
s = sounds.Sound(dir / "heartbeat.wav")
wait_finish(s.play())
s2 = sounds.Sound(dir / "buzz.wav")
wait_finish(s2.play())
s3 = sounds.Sound(dir / "ohno.wav")
wait_finish(s3.play())
s4 = sounds.Sound(dir / "carhorn.wav")
wait_finish(s4.play())
