import random

while True:
    choice = input("Roll the dice?(y/n):").lower()

    if choice == "n":
        print("Goodbye!")
        break
    elif choice == "y":
        print("You rolled",random.randint(1,6))

    else:
        print("Please enter y or n")     