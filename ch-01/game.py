from random import randint
secret = randint(1, 10)

print("Welcome!")
guess = 0
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You win!")
        break
    if guess > secret:
        print("Too high!")
    else:
        print("Too low!")
print("Game over!")
