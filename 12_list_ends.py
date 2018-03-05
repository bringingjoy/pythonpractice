###############################################################################
# Exercise 12:  List Ends (PracticePython)
# Author:       Jenny Hamer
# 
# Description:  Write a program that takes a list of numbers 
#               (e.g., a = [5, 10, 15, 20, 25]) and makes a new list composed
#               of the first and last elements of the given list. (For practice,
#               write code as a function).
###############################################################################

def list_ends(num_list):
    
    new_list = []
    new_list.append(num_list[0])
    if len(num_list) > 1:
        new_list.append(num_list[-1])
    return new_list

test_list = [5*x for x in range(1, 6)]
new_list = list_ends(test_list)

print("The original list:", test_list)
print("The list-ends list:", new_list)
