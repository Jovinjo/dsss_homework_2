import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculator


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operators
            random_operator = generate_random_operator()
            self.assertIn(random_operator, operators)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 5, '-', '8 - 5', 3),
                (5, 3, '*', '5 * 3', 15),
                (2, 4, '+', '2 + 4', 6),
                (3, 3, '*', '3 * 3', 9),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculator(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
