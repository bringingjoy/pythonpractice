###############################################################################
# Exercise 3:  List Less Than Ten (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Given a list, print out all of its elements which are less than 
#              10.
###############################################################################

# user_list = list(input("Please enter a list of numbers: "))


example_list = [1, 2, 3, 4, 5, 6, 16, 15, 14, 13, 12, 11, 10]
less_than_ten = [x for x in example_list if x < 10]
print("This is the list which contains all elements of your list which are less \
than 10", less_than_ten)
