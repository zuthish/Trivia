import requests
# import html
import random
import sys
import time
from termcolor import colored
from colorama import Style,init




s = colored("Welcome to Trivia!","magenta")
p = f"{Style.BRIGHT}{s}{Style.RESET_ALL}"
for char in p:
    print(char,end='')
    sys.stdout.flush()
    time.sleep(0.1)
print()



# Get a pool of trivia questions
def get_question(amount,category):
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]


# shuffle the answer choices for a question
def shuffling(choices):
    random.shuffle(choices)
    return choices
    

# Print the answer choices in the terminal
# def display_choices(choices):
#     for choices_index , choice in enumerate(choices):
#         print(f"{choice_index + 1}.{html.unescape(choice)}")


# Get user's choice in terminal 



# play the game



# call main function
