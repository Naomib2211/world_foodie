import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# Quiz Questions and Multiple Choices

food_questions = (
    "Which country is famous for its traditional dish of 'Pho'?: ",
    "What is the main ingredient in the indian dish 'Samosa'?: ",
    "What food is Peru known for?",
    "Which country is the origin of the dish 'Moussaka'?: ",
    "What dish is Switzerland famous for?: ",
    "What is the traditional breakfast food in Jamaica?: ",
    "Which country is renowned for its traditional dish called 'Pierogi'?: ",
    "What food is Argentina famous for?: ",
    "What is the national dish of Brazil?: ",
    "Which country is known for its traditional dish of 'Borscht'?: "
)

food_questions_number = 0

mult_choices = (
    ("1. Japan", "2. Vietnam", "3. Thailand", "4. China"),
    ("1. Rice", "2. Potatoes", "3. Noodles", "4. Tofu"),
    ("1. Sushi", "2. Tacos", "3. Ceviche", "4. Hamburger"),
    ("1. Greece", "2. Turkey", "3. Egypt", "4. Marocco"),
    ("1. Fondue", "2. Kimchi", "3. Pizza", "4. Sushi"),
    ("1. Baguette", "2. Roti", "3. Jerk chicken", "4. Ackee and saltfish"),
    ("1. Poland", "2. Hungary", "3. Czech Republic", "4. Slovakia"),
    ("1. Empanadas", "2. Sushi", "3. Pho", "4. Tacos"),
    ("1. Pad Thai", "2. Feijoada", "3. Kimchi", "4. Gyros"),
    ("1. Russia", "2. France", "3. Italy", "4. Spain")
    )

correct_answer = ("2", "2", "3", "1", "1", "4", "1", "1", "2", "1")

# Function to start quiz


def conduct_quiz(food_questions, mult_choices, correct_answer):
    while True:
        score = 0
        total_food_questions = len(food_questions)
        users_answers = []

        print(Back.GREEN + Style.BRIGHT + "Welcome to the World Foodie Quiz!")
        print("\nIt's simple!"
              "\nAnswer the question by typing \nin the letter"
              " that corresponds \nto the 'right' answer.")

        food_questions_order = list(range(total_food_questions))
        random.shuffle(food_questions_order)

        for i in food_questions_order:
            print(Fore.BLUE + Style.BRIGHT +
                  f"\nQuestion: {food_questions[i]}")
            print(Fore.YELLOW + "Choices: ")
            for choice in mult_choices[i]:
                print(Style.BRIGHT + choice)

            # Validate user input
            while True:
                user_answer = input(f"\nYour answer:\n ")
                if user_answer in ["1", "2", "3", "4"]:
                    users_answers.append(user_answer)
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "Invalid answer! "
                          "Please choose between numbers 1, 2, 3 or 4")

        print("\nQuiz completed!\nHere is your result: ")

        # Calculate user score
        for user_answer, correct_answer in zip(users_answers, correct_answer):
            if user_answer == correct_answer:
                score += 1
        print(f"\nTotal Points: {score}")

        # Display message to user based on score
        if score <= 3:
            print("Well... \nThe good part is that you get to explore"
                  "\nwhat the world has to offer!")
        elif 4 <= score <= 6:
            print("Pretty average! Nothing else to say, really.")
        else:
            print("Congratulations! This is general knowledge,"
                  "\nbut good for you!")

        # Prompt user to restart the quiz
        while True:
            restart = input(Fore.CYAN +
                            "\nDo you want to restart the quiz? (yes/no):"
                            + Style.RESET_ALL + "\n ").lower()
            if restart == "yes":
                print(Fore.MAGENTA + "\nRestarting the quiz...\n")
                break
            elif restart == "no":
                print(Back.GREEN + Style.BRIGHT +
                      "\n Thank you for taking this quiz! Bye! "
                      + Back.RESET + Style.RESET_ALL)
                return
            else:
                print(Fore.RED + Style.BRIGHT +
                      "Invalid answer, please type 'yes' or 'no'.")

if __name__ == '__main__':
    conduct_quiz(food_questions, mult_choices, correct_answer)
