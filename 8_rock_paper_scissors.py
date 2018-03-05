###############################################################################
# Exercise 8:  Rock-Paper-Scissors (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Write a two-player Rock-Paper-Scissors game. Ask if user wants
#              to play against another player or the computer, and how many
#              rounds to play (i.e. best 2 out of 3).
###############################################################################

import random

while True:
    try:
        num_rounds = int(input("How many rounds would you like to play? (e.g. 3 for best 2/3) "))
        break
    except ValueError:
        print("Uh oh, that wasn't a valid number - please try again.")

play_against = input("Please enter 'yes' if you would like to play against the computer, 'no' to play against yourself: ") 

rules = ["Rock", "Paper", "Scissors"]

if play_against == 'yes':

    num_turns = 0
    user_score = 0
    while num_turns < num_rounds:

        # Get User input and type check
        while True:
            try:
                user_choice = int(input("Please pick: 1 for Rock, 2 for Paper, 3 for Scissors: ")) - 1
                break
            except ValueError:
                print("That wasn't quite right; please try again.")
        print("You choose:", rules[user_choice])
        comp_choice = random.randint(0, 2)
        print("Computer chooses:", rules[comp_choice])
        
        # If User: Rock, Comp: Scissors or User: Paper, Comp: Rock, or User: Scissors, Comp: Paper
        if (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
            print("+1 for you!")
            num_turns += 1
            user_score += 1
        # If User and Comp choose same "weapon"            
        elif user_choice == comp_choice:
            print("Round draw!")
        # Otherwise, Comp won this round...
        else:
            print("+1 for Computer!")
            num_turns += 1

    if user_score >= num_rounds-1:
        print("Congratulations, you win!")
    else:
        print("Sorry, you lost...")            
