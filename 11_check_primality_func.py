###############################################################################
# Exercise 11:  Check Primality Functions (PracticePython)
# Author:       Jenny Hamer
# 
# Description:  Prompt the user for a number and determine whether or not it
#               is prime. Return the result.
###############################################################################

# Given num, an integer, try dividing it by all numbers between [2, num)
def get_divisor(num):

    possible_divisors = [x for x in range(2, num)]
#    print(possible_divisors)
    prime = True
    for x in possible_divisors:
        if num % x == 0:
            prime = False
            print("Looks like", num, "is composite!", x, "divides it.")
            break
    print("We found no divisors of", num, "besides 1 and itself. It's a prime!")


while True:
    try:
        user_val = int(input("Please enter a number to check whether it is prime: "))
        break
    except ValueError:
        print("Looks like you didn't enter a valid number. Please try again...")

get_divisor(user_val)
