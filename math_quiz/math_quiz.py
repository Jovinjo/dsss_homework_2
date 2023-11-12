import random


def generate_random_integer(min, max):
    """
    Parameters:
    - min (int): The minimum value of the range.
    - max (int): The maximum value of the range.
    Returns:
    - int: A randomly generated integer.
    """
    # generate random number between min and max
    return random.randint(min, max)


def generate_random_operator():
    """
    Returns:
    - str: A randomly selected arithmetic operator.
    """
    # generate random operator
    return random.choice(['+', '-', '*'])


def calculator(number1, number2, operator):
    """
    Parameters:
    - number1 (float): The first number.
    - number2 (float): The second number.
    - operator (str): The arithmetic operator ('+', '-', '*').

    Returns:
    - f-str: the math question
    - int: result
    """
    # calculate result of mathematical expression
    expression = f"{number1} {operator} {number2}"
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return expression, result

def get_user_input():
    while True:
        try:
            user_input = int(input("Your answer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter again a valid integer!")

def math_quiz():
    """
    A math quiz game where users answer a random generated math problem
    User get a point everytime a correct answer is given and if wrong the result will be display
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # generate random integer and operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        op = generate_random_operator()

        # calculate the answer
        problem, answer = calculator(num1, num2, op)

        # display the math question
        print(f"\nQuestion: {problem}")

        # User giving answer
        user_answer = get_user_input()

        # Check matching answer
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
