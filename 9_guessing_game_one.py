###############################################################################
# Exercise 9:  Guessing Game One (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Generate a random number between 1 and 9 (including 1 and 9). 
#              Ask the user to guess the number, then tell them whether they 
#              guessed too low, too high, or exactly right.
###############################################################################

# Random number generator import
import random


bounds = [1, 9]     # Guess bounds
# Loop game until player enters 'exit'
playing = True
while playing:

    num_to_guess = random.randint(1, 9)
    num_tries = 0
    won = False
    while not won:
    
    # Type check user input
#    while True:
#        try:
#            user_guess = int(input("Enter your guess (between 1 - 9), or 'exit' to end game: "))
#            break
#        except ValueError:
#            print("Uh oh, that wasn't a valid number. Please try again...")

        user_guess = input("Enter your guess (between 1 and 9), or 'exit' to end game: ")
        if user_guess == 'exit':
            print("Thank you for playing!")
            playing = False
            break
        user_guess = int(user_guess)
        if user_guess > bounds[1] or user_guess < bounds[0]:
            print("That guess was out of bounds! Please guess again.")
        elif user_guess > num_to_guess:
            num_tries += 1
            print("Your guess was too high")
        elif user_guess < num_to_guess:
            num_tries += 1
            print("Your guess was too low") 
        else:
            num_tries += 1
            won = True
            print("Your guess was just right! You won in", num_tries, "!")
