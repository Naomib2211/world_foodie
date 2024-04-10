import random

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

food_question_number = 0

mult_choices = (
    ("1. Japan”, “2. Vietnam”, “3. Thailand”, “4. China"),
    ("1. Rice”, “2. Potatoes”, “3. Noodles”, “4. Tofu"),
    ("1. Sushi”, “2. Tacos”, “3. Ceviche”, “4. Hamburger"),
    ("1. Greece”, “2. Turkey”, “3. Egypt”, “4. Marocco"),
    ("1. Fondue”, “2. Kimchi”, “3. Pizza”, “4. Sushi"),
    ("1. Baguette”, “2. Roti”, “3. Jerk chicken”, “4. Ackee and saltfish"),
    ("1. Poland”, “2. Hungary”, “3. Czech Republic”, “4. Slovakia"),
    ("1. Empanadas”, “2. Sushi”, “3. Pho”, “4. Tacos"),
    ("1. Pad Thai”, “2. Feijoada”, “3. Kimchi”, “4. Gyros"),
    ("1. Russia”, “2. France”, “3. Italy”, “4. Spain"),  
)

correct_mult_choice = ("2", "2", "3", "1", "1", "4", "1", "1", "2", "1")
print(mult_choices)