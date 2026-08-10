import random

secret = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == secret:
    print("You guessed it!")
elif guess < secret:
    print("Too low.")
else:
    print("Too high.")
# ...existing code...

