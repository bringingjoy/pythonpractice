###############################################################################
# Exercise 6:  String Lists (PracticePython)
# Author:      Jenny Hamer
# 
# Description: Prompt the user for a string and print out whether this string
#              is a palindrome or not.
# Notes:       Strings are lists in Python (
###############################################################################


user_str = input("Please enter a string: ")

len_str = len(user_str)
for i in range(len_str):
#    if len_str % 2 == 0:
    if not user_str[i] == user_str[-1 -i]:
        print("This string is not a palindrome")
        break
    elif i == int(len_str / 2):
        print("This string *is* a palindrome!")

