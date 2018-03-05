###############################################################################
# Exercise 5:  List Overlap (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Given two lists, return a list which contains only the common 
#              elements of the two lists (without duplicates). 
###############################################################################

import random

print("We are going to experiment with random lists!")

while True:
    try:
        len_list_1 = int(input("Please enter the length of the first list: "))
        len_list_2 = int(input("Please do the same for the second list: "))
        max_val = int(input("What is the maximum value you would like to see in a given list? "))
        break
    except ValueError:
        print("Oops, something you entered was not a valid number. Please try again...")

list_1 = [random.randint(1, max_val) for i in range(len_list_1)]
list_2 = [random.randint(1, max_val) for i in range(len_list_2)]

print("The first random list is:", list_1)
print("The second is:", list_2)

max_len = len_list_1 if len_list_1 > len_list_2 else len_list_2
print("Max. len", max_len)

# common_list = [x for x in list_1 if x in list_2 and x not in x]
common_list = []
for x in list_1:
    if x in list_2 and x not in common_list:
        common_list.append(x)
print("The common elements are", common_list)

