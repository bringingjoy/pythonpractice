###############################################################################
# Exercise 18: Cows and Bulls (PracticePython)
# Author:      Jenny Hamer
# 
# Description: This program plays the "cows and bulls" game with the user, which
#              randomly generates a 4-digit number for the user to guess. Then,
#              for every digit guessed correctly in the correct place is a "cow";
#              every digit guessed correctly in the wrong place is a "bull".
#              After every guess, the user is updated with their # of each.
#              The user wins when they correctly guess the number.
#              
###############################################################################



import random

def gen_four_digit_num():
    num_as_string = ""
    for i in range(4):
        num_as_string += str(random.randint(0, 10))
    return num_as_string
#    num_to_guess = int(num_as_string)
#    return num_to_guess

def get_user_guess():

    user_guess = input("Enter your guess: ")
    return user_guess
#    while True:
#        try:
#            user_guess = int(input("Enter your guess: "))
#            break
#        except ValueError:
#            print("Looks like that wasn't a number; please try again...")
#    return user_guess

def get_cows_bulls(num_to_guess, user_guess):
    
    num_cows = 0
    num_bulls = 0
    for i in range(4):
        if user_guess[i] == num_to_guess[i]:
            num_cows += 1
        elif user_guess[i] in num_to_guess:
            num_bulls += 1
    print(num_cows, "cows", num_bulls, "bulls") 

def main():
    num_to_guess = gen_four_digit_num()
    # For DEBUG:
#    num_to_guess = "1359"
    player_won = False
    num_guesses = 0
    while not player_won:
        curr_guess = get_user_guess()
        num_guesses += 1
        # If the player guessed correctly
        if (curr_guess == num_to_guess):
            player_won = True
            print("You won in", num_guesses, "guesses!")
            break
        get_cows_bulls(num_to_guess, curr_guess)
    
if __name__ == "__main__":
    main()
