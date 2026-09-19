import random

secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct! 🎉")
        print("You got it in", attempts, "attempts!")
        break