print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
    print("You win!")
elif guess > 5:
    print("Too high!")
    print("You lose!")
else:
    print("Too low!")
    print("You lose!")
print("Game over!")
