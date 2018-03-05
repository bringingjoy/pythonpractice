###############################################################################
# Exercise 4:  Divisors (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Ask the user for a number; then, print out all divisors of that
#              number.
###############################################################################


while True:
    try:
        user_num = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oh no, that's not a valid number! Please try again...")

print_style = input("Please enter 'yes' to see the numbers one by one, 'no' to see them in a list: ")
possible_divisors = range(2, user_num)
divisors = [x for x in possible_divisors if user_num % x == 0]

print("Here is a list of numbers which divide", user_num)

if print_style.lower() == "no":
    print(divisors)
else: 
    for i in range(len(divisors)):
        print(divisors[i])
