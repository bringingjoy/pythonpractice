###############################################################################
# Exercise 13: Fibonacci (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Prompt the user to enter the number of desired Fibonnaci numbers
#              to generate, then generate them. (Naive method & less-naive/DP-ish)
###############################################################################

def generate_fib(running_list):
    # Generate the next Fibonacci number in the sequence and add it to the
    # running_list of numbers and return the next Fibonacci #
    
    next_fib = running_list[-1] + running_list[-2]
    return next_fib


while True:
    try:
        num_fib = int(input("Please enter the number of Fibonacci numbers to generate: "))
        break
    except ValueError:
        print("Please enter a valid (positive) number.")

list_of_fib = [1, 1]
for i in range(num_fib):
    list_of_fib.append(generate_fib(list_of_fib))

print(list_of_fib)
