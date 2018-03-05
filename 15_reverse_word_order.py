###############################################################################
# Exercise 15: Reverse Word Order (PracticePython)
# Author:      Jenny Hamer
# 
# Description: This is a function which prompts the user for a long string 
#              (containing multiple words), then prints the string in backwards
#              order.
###############################################################################


def get_user_str():
    # Get and return a string containing 2+ words from the user    

    user_str = ""
    while True:
        user_str = input("Please enter a sentence, phrase, or series of words: ")
        # Check that input is non-trivial
        if len(user_str.split(" ")) < 2:
            print("Please enter a longer sentence (2+ words)")
        else:
            break
    return user_str

def reverse_user_str(user_str):
    # Split the input string at " " characters and add each word to a new string in
    # reversed order using list indexing (strings are lists in Python)

    split_str = user_str.split(" ")
    new_str = ""
    for i in range(len(split_str)):
        new_str += split_str[-1-i] + " "
    return new_str

print("Get ready for some fun string action!")
string = get_user_str()
print("Your reversed string:\n", reverse_user_str(string))
   

# Sample output:
# Get ready for some fun string action!
# Please enter a sentence, phrase, or series of words: Here is an example!
# Your reversed string:
# example! an is Here  
