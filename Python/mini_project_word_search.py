'''
In this project, you are tasked to create a program that automates searching for a word definition in a dictionary. Follow the instructions to implement



Dictionary Project is provided here in data.json file.

We should have a data source (data.json) that contains a dictionary of words and their meanings.
Learn how to load json data into a python dictionary
Create a function that returns a definition of a word
Consider a condition that the entered word is not in a dictionary
Consider input from user having different cases – upper/ lower case or mixed eg: RAIN/rain/RaIN
Make your dictionary program more intelligent incase users input a word with wrong spelling the program should be able to suggest the word that might be intended.
eg . pott instead of pot or rainn instead of rain. Tip: use difflib library here
'''

# Importing the necessary libraries
import json
from difflib import get_close_matches

# Loading the data from the json file
data = json.load(open("data.json"))

# Function to get the definition of the word
def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
        decide = input("Press 'Y' for Yes and 'N' for No: ")
        if decide == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# Taking the input from the user
if __name__ == "__main__":
    word = input("Enter the word: ")
    while word != "exit":
        print(get_definition(word))
        word = input("Enter the word: ")
    print("Thank you for using the dictionary.")

# End of Program
