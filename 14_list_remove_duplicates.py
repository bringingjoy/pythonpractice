###############################################################################
# Exercise 14: List Remove Duplicates (PracticePython)
# Author:      Jenny Hamer
# 
# Description: This is a function which takes a list and returns a new list
#              containing the unique elements of the original list.
###############################################################################

def exclude_duplicates(orig_list):

    new_list = []
    for x in orig_list:
        if x not in new_list:
            new_list.append(x)

    return new_list

def exclusion_via_sets(orig_list):
    
    new_list = [x for x in set(orig_list)]
    return new_list


test_list = [x*2 for x in range(1, 11)]
test_list.append(2)
test_list.append(12)

print("Original list:", test_list)

print("Without duplicates (list manner):", exclude_duplicates(test_list))
print("Without duplicates (using sets):", exclusion_via_sets(test_list))
