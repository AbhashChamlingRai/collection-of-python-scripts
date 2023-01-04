"""
Write a Python script that prompts the user to enter their marks and determines their letter grade based on the following criteria:

    -If the marks are less than 25, the letter grade is 'F'
    -If the marks are greater than or equal to 25 and less than 45, the letter grade is 'E'
    -If the marks are greater than or equal to 45 and less than 50, the letter grade is 'D'
    -If the marks are greater than or equal to 50 and less than 60, the letter grade is 'C'
    -If the marks are greater than or equal to 60 and less than 80, the letter grade is 'B'
    -If the marks are greater than or equal to 80, the letter grade is 'A'

The script should print the appropriate letter grade to the console.
"""

def first_method(user_marks):
    """
    This function uses "and" operator
    """
    if user_marks < 25:
        return "Your grade is 'F'"
    elif user_marks >= 25 and user_marks < 45:
        return "Your grade is 'E'"
    elif user_marks >= 45 and user_marks < 50:
        return "Your grade is 'D'"
    elif user_marks >= 50 and user_marks < 60:
        return "Your grade is 'C'"
    elif user_marks >= 60 and user_marks < 80:
        return "Your grade is 'B'"
    elif user_marks >= 80:
        return "Your grade is 'A'"

def second_method(user_marks):
    """
    This function uses range() to calculate grade
    """
    if user_marks in range(0, 25):
        return "Your grade is 'F'"
    elif user_marks in range(25, 45):
        return "Your grade is 'E'"
    elif user_marks in range(45, 50):
        return "Your grade is 'D'"
    elif user_marks in range(50, 60):
        return "Your grade is 'C'"
    elif user_marks in range(60, 80):
        return "Your grade is 'B'"
    elif user_marks >= 80:
        return "Your grade is 'A'"

def third_method(user_marks):
    """
    This function is the simplest one
    """
    if user_marks >= 80:
        return "Your grade is 'A'"
    elif user_marks >= 60:
        return "Your grade is 'B'"
    elif user_marks >= 50:
        return "Your grade is 'C'"
    elif user_marks >= 45:
        return "Your grade is 'D'"
    elif user_marks >= 25:
        return "Your grade is 'E'"
    elif user_marks < 25:
        return "Your grade is 'F'"

if __name__ == "__main__":
    user_given_marks = int(input("\nEnter your marks: "))
    print(f"\n-Marks using first method: {first_method(user_given_marks)}")
    print(f"\n-Marks using second method: {second_method(user_given_marks)}")
    print(f"\n-Marks using third method: {third_method(user_given_marks)}")

