import random


def get_random_int(min, max):
    """
    Generates a random integer between the integers called min and max (inclusive).

    Parameters:
    min (int): The lower bound of the range.
    max (int): The upper bound of the range.

    Returns:
    int: A random integer between min and max.
    """

    return random.randint(min, max)


def get_random_operand():
    """
    Generates random arithmetic operation.

    Returns:
    str: A random arithmetic operation.
    """

    return random.choice(['+', '-', '*'])


def arithmetic_operation(number_1, number_2, operand):
    """
    Performs an arithmetic operation on two integers.

    Parameters:
    number_1 (int): The first integer.
    number_2 (int): The second integer.
    operand (str): The arithmetic operation to perform.

    Returns:
    tuple: A tuple containing the string representation of the arithmetic operation and the result.
    """
    # Create a string representation of the arithmetic operation
    calculation = f"{number_1} {operand} {number_2}"

    # Check which arithmetic operation is requested
    if operand == '+': result = number_1 + number_2 # Addition
    elif operand == '-': result = number_1 - number_2 # Subtraction
    else: result = number_1 * number_2 # Multiplication
    
    # Return the string representation of the arithmetic operation and the result
    return calculation, result

def math_quiz():
    """
    A math quiz game that asks the user to solve math problems. The game
    consists of 3 math problems, and the user earns a point for each correct
    answer. In the end, the game displays the user's score.

    """
    user_score = 0  # Initialize the user's score to 0
    repetitions = 3 # Number of math problems

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the math problems
    for _ in range(repetitions):
        try:
            number_1 = get_random_int(1, 10)    # Generate a random integer between 1 and 10
            number_2 = get_random_int(1, 5)   # Generate a random integer between 1 and 5
            operand = get_random_operand()      # Generate a random arithmetic operand
        except Exception as e:
            print(f"An error occurred whilst generating the two random numbers and the operand: {e}")
            continue

        try:
            # Get the arithmetic operation and the result of it
            PROBLEM, ANSWER = arithmetic_operation(number_1, number_2, operand)
        except Exception as e:
            print(f"An error occurred whilst performing the arithmetic operation: {e}")
            continue

        print(f"\nQuestion: {PROBLEM}")
        # Get the user input via the console
        useranswer = input("Your answer: ")
        
        try:
            # Check if the user's input is a valid integer
            if not useranswer.isdigit():
                raise ValueError("Please enter a valid integer.")
            useranswer = int(useranswer)
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            user_score += 1 # Increment the user's score by 1
        else:
            # Display the correct answer if the user's answer is wrong
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # Displays how many answers out of the problems the user got right
    print(f"\nGame over! Your score is: {user_score}/{repetitions}")

if __name__ == "__main__":
    # Run the math quiz game
    math_quiz()
