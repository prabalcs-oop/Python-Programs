

# ...existing code...
import random

secret = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if guess == secret:
        print("You guessed it!")
        break
    elif guess < secret:
        print("Too low.")
    else:
        print("Too high.")
# ...existing code...
