import unittest
from unittest.mock import patch
from io import StringIO
import random

from run import conduct_quiz, food_questions, mult_choices, correct_answer

class TestQuiz(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        'invalid',  # Invalid input for question
        '1', '2', '3', '4', '1', '2', '3', '4', '1', '2',  # Valid inputs for 10 questions
        'no'  # End the quiz
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_question(self, mock_stdout, mock_input):
        conduct_quiz(food_questions, mult_choices, correct_answer)
        output = mock_stdout.getvalue()
        
        # Check for invalid input message for quiz question
        self.assertIn("Invalid answer! Please choose between numbers 1, 2, 3 or 4", output)


    @patch('builtins.input', side_effect=['1', '2', '3', '4', '1', '2', '3', '4', '1', '2', 'no'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_conduct_quiz_no_restart(self, mock_stdout, mock_input):
        conduct_quiz(food_questions, mult_choices, correct_answer)
        output = mock_stdout.getvalue()

        self.assertIn("Total Points:", output)
        self.assertIn("Thank you for taking this quiz! Bye!", output)

    @patch('builtins.input', side_effect=[
        '1', '2', '3', '4', '1', '2', '3', '4', '1', '2', 
        'yes',
        '1', '2', '3', '4', '1', '2', '3', '4', '1', '2',
        'no'
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_conduct_quiz_yes_restart(self, mock_stdout, mock_input):
        conduct_quiz(food_questions, mult_choices, correct_answer)
        output = mock_stdout.getvalue()

        self.assertIn("Total Points:", output)  
        self.assertIn("Restarting the quiz...", output)  
        self.assertIn("Thank you for taking this quiz! Bye!", output)

if __name__ == '__main__':
    unittest.main()


