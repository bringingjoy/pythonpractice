###############################################################################
# Exercise 1: Character Input (PracticePython)
# 
# Description: Ask the user to enter their name and age. Print out a message
#              addressed to them that tells them the year that they will turn 
#              100 years old.
###############################################################################


user_name = input("Please enter your name: ")
user_age = input("Please enter your age: ")

try_again = True
while try_again:
    try:
        user_age = int(input("Please enter your age: ")) 
        try_again = False
        break
    except ValueError:
        print("Oh no, the age you entered was not a valid number. Please try again. ")

year_100 = 100 - user_age + 2018
print("Hello,", user_name)
print("You will turn 100 in the year", year_100)
