import unittest
from unittest.mock import patch
from io import StringIO
import random

from run import conduct_quiz, food_questions, mult_choices, correct_answer

class TestQuiz(unittest.TestCase):
    #1. Test for invalid input during questions
    @patch('builtins.input', side_effect=[
        'yes',
        'invalid',  
        '1', '2', '3', '4', '1', '2', '3', '4', '1', '2',  
        'no'  
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_question(self, mock_stdout, mock_input):
        conduct_quiz(food_questions, mult_choices, correct_answer)
        output = mock_stdout.getvalue()
        
        self.assertIn("Invalid answer! Please choose between numbers 1, 2, 3 or 4", output)

    #2. Test quiz completion without restart
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '1', '2', '3', '4', '1', '2', 'no'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_conduct_quiz_no_restart(self, mock_stdout, mock_input):
        conduct_quiz(food_questions, mult_choices, correct_answer)
        output = mock_stdout.getvalue()

        self.assertIn("Total Points:", output)
        self.assertIn("Thank you for taking this quiz! Bye!", output)

    #3. Test quiz with restart
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

    #4. Test with all correct answers
    @patch('builtins.input', side_effect=[
        '2', '2', '3', '1', '1', '4', '1', '1', '2', '1',
        'no'
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_conduct_all_scores_correct(self, mock_stdout, mock_input):
        conduct_quiz(food_questions, mult_choices, correct_answer)
        output = mock_stdout.getvalue()

        self.assertIn("Total Points: 10", output)
        self.assertIn("Congratulations! This is general knowledge,"
              "\nbut good for you!", output)
        
    #5. Test with all incorrect answers
    @patch('builtins.input', side_effect=[
        '1', '1', '1', '2', '3', '1', '2', '3', '3', '2',  
        'no'
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_all_incorrect_answers(self, mock_stdout, mock_input):
        conduct_quiz(food_questions, mult_choices, correct_answer)
        output = mock_stdout.getvalue()

        
        self.assertIn("Total Points: 0", output)
        self.assertIn("Well... \nThe good part is that you get to explore"
                      "\nwhat the world has to offer!", output)        

if __name__ == '__main__':
    unittest.main()


