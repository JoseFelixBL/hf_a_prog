import pygame.mixer
from pathlib import Path

sounds = pygame.mixer
sounds.init()


def wait_finish(channel):
    while channel.get_busy():
        pass


dir = Path('ch-07')
correct_s = sounds.Sound(dir / "correct.wav")
wrong_s = sounds.Sound(dir / "ohno.wav")

prompt = "Press 1 for correct, 2 for wrong or 0 to Quit: "
number_right = 0
number_wrong = 0
# number_asked = 0
while True:
    response = input(prompt)
    if response == '0':
        break
    if response == '1':
        number_right += 1
        wait_finish(correct_s.play())
    elif response == '2':
        number_wrong += 1
        wait_finish(wrong_s.play())
    else:
        print("Invalid input")
        continue
    # number_asked += 1

print(
    f"Correct: {number_right}, Wrong: {number_wrong}, Asked: {number_wrong + number_right}")
