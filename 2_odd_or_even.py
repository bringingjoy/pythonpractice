###############################################################################
# Exercise 2:  Odd or Even (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Ask the user for a number. Depending on whether the number is
#              odd or even, print out an appropriate message to the user.
###############################################################################


user_num = input("Enter a number: ")
parity = int(user_num) % 2
if parity == 0:
    print("The number", user_num, "is even")
else:
    print("The number", user_num, "is odd")
