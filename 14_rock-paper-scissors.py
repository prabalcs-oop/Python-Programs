import random

choices = ["rock","paper","scissors"]

while True:
    user = input("Choose rock,paper,scissors, or quit:").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice.")
        continue

    computer = random.randint(choices)
    print("computer choose:",computer)

    if user == computer:
        print("It's Draw!//")
    elif(user == "rock" and computer == "scissors")or\
    (user == "paper" and computer == "rock")or\
    (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("computer woins!")    