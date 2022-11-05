# Learning Activity - Password.py
# by Louie Candelario
# 15/10/2022
import random


stored_number = random.randint(1, 10)
number_of_tries = 0
previous_guess = int

print("Guess a number between 1 and 10")
guess = int(input("enter the number of your guess"))

while True:
    if guess > stored_number:
        number_of_tries += 1
        print("Sorry. Try Again. The number is smaller than your guess. ")
            if previous_guess != guess:

            guess = int(input("enter the number of your guess"))
    elif guess < stored_number:
        number_of_tries += 1
        print("Sorry. Try Again. The number is larger than your guess. ")
        previous_guess = guess
        guess = int(input("enter the number of your guess"))
    elif guess == previous_guess and guess > stored_number:
        print("Sorry. Try Again. No tries added. The number is smaller than your guess")
        previous_guess = guess
        guess = int(input("enter the number of your guess"))
    elif guess == previous_guess and guess < stored_number:
        print("Sorry. Try Again. No tries added. The number is larger than your guess")
        previous_guess = guess
        guess = int(input("enter the number of your guess"))
    elif guess == stored_number:
        number_of_tries += 1
        print("You got it!")
        print("Number of tries", number_of_tries)
        break

exit = input("hit enter to exit")




