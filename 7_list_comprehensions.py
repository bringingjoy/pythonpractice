###############################################################################
# Exercise 6:  List Comprehensions (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Given a list, return a new list containing only the even elements
#              of the original list (in one line of code).
###############################################################################

given_list = [x**2 for x in range(1, 11)]
even_list = [x for x in given_list if x % 2 == 0]

print("The given list:", given_list)
print("The subset list containing only even elements:", even_list)
