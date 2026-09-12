secret_number = 7

print("Guess the Secret Number!")
print("Try to guess the number between 1 and 10.")

while True:
    try:
        guess = int(input("Guess the number: "))

        if guess == secret_number:
            print("Correct! You guessed it!")
            break
        else:
            print("Wrong guess! Try again.")

    except ValueError:
        print("Please enter a valid number.")