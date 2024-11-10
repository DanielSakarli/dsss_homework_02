import unittest
from math_quiz import get_random_int, get_random_operand, arithmetic_operation

class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operand(self):
        # Test if random operand generated is either '+', '-', or '*'

        for _ in range(1000):  # Test a large number of method calls
            operand = get_random_operand()
            self.assertTrue(operand == '+' or operand == '-' or operand == '*')

    def test_arithmetic_operation(self):
            test_cases = [
                 # These cases will be tested if they are correctly calculated
                 # by the arithmetic_operation function
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (1, 1, '+', '1 + 1', 2),
                (1, 1, '-', '1 - 1', 0),
                (1, 1, '*', '1 * 1', 1),
                (4, 3, '+', '4 + 3', 7),
                (4, 3, '-', '4 - 3', 1),
                (4, 3, '*', '4 * 3', 12),
                (8, 2, '+', '8 + 2', 10),
                (8, 2, '-', '8 - 2', 6),
                (8, 2, '*', '8 * 2', 16),
                (9, 3, '+', '9 + 3', 12),
                (9, 3, '-', '9 - 3', 6),
                (9, 3, '*', '9 * 3', 27),
            ]

            # Test each case
            for number_1, number_2, operand, expected_problem, expected_answer in test_cases:
                problem, answer = arithmetic_operation(number_1, number_2, operand)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
