print("Welcome to Jorge's 'guess the number' game!")
print("I have in mind a number between 1 and 100. Can you guess what it is?")

import random
random.randrange(1, 101)

number_guess = random.randrange(1, 101)
chances = 0

while chances < 100000:
    user_guess = int(input("Type your guess: "))
    if user_guess == number_guess:
        print("You smart cookie! Sorry, I don't have anything to give you.")
        break

    elif user_guess > number_guess:
        print("Are you trying to pull my leg? Guess lower.")

    else:
        print("The number I have in mind is higher.")
