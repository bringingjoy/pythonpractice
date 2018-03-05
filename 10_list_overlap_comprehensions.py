###############################################################################
# Exercise 10:  List Overlap with List Comprehensions! (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Given two lists, return a list which contains only the common 
#              elements of the two lists (without duplicates) using 
#              *list comprehension*. 
###############################################################################


import random

len_1 = int(input("Please enter the length of the first list: "))
len_2 = int(input("Please enter the length of the second list: "))
rand_max = int(input("Please enter the max random value you want in either list: "))

rand_list_1 = [random.randint(1, rand_max) for i in range(len_1)]
rand_list_2 = [random.randint(1, rand_max) for i in range(len_2)]

# rand_list_1 = random.sample(range(rand_max), len_1)
# rand_list_2 = random.sample(range(rand_max), len_2)

common_list = [i for i in set(rand_list_1) if i in rand_list_2]
print("Output using set:", common_list)

# Same result?
overlap_list = []
for num in common_list:
    if num not in overlap_list:
        overlap_list.append(num)
print(overlap_list)
