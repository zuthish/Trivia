import requests
import html
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
def display_choices(choices):
    for choices_index , choice in enumerate(choices):
        print(f"{choices_index + 1}.{html.unescape(choice)}")


# Get user's choice in terminal 
def get_user_choice(num_choices):
    while True:
        try:
            choice = int(input("Enter your answer(number): "))
            if 1 <= choice <= num_choices:
                print(f"Please enter a number between 1 and {num_choices}")
        except ValueError:
            print        


# play the game
def play_game(amount,category):
    questions = get_question(amount,category)
    score = 0

    for i , question in enumerate(questions,1):
        print(f"\nQuestion {i}/ {amount}:")
        print(html.unescape(question["question"]))

        all_choices = [question["correct_answer"]] + question["incorrect_answers"]
        shuffled_choices = shuffling(all_choices.copy())

        display_choices(shuffled_choices)

        user_choice = get_user_choice(len(shuffled_choices))

        correct_answer = question["correct_answer"]
        user_answer =shuffled_choices[user_choice -1]

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The Correct answer was: {html.unescape(correct_answer)}")

            time.sleep(1)
    print("\n" + "="*40)
    print(f"Final Score: {score}/{amount}")
    percentage = (score/amount)*100
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Perfect score! Amazing job! ")
    elif percentage >= 80:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job! Keep practicing")
    else:
        print("Keep trying, you'll improve!")
    print("="*40)

# call main function
def main():
    categories = {
        "General Knowledge": 9,
        "Books": 10,
        "Film": 11,
        "Music": 12,
        "Science": 17,
        "Computers": 18,
        "Mathematics": 19,
        "Sports": 21,
        "Geography": 22,
        "History": 23,
        "Politics": 24,
        "Art": 25
    }

    print("\nAvailable Categories:")
    for i, (category,_) in enumerate(categories.items(), 1):
        print(f"{i}.{category}")

    while True:
        try:
            choice = int(input("\nSelect a category (number): "))
            if 1 <= choice <= len(categories):
                category_id = list(categories.values()) [choice - 1]
                break
            print(f"Please enter a number between 1 and {len(categories)}")
        except ValueError:
            print("Please enter a valid number")    


if __name__ == "__main__":
    main()