"""
5.2 Create in Python the program which must:
a. show the contents of the math module
b. show the help of the functions used to perform the following calculations:
    • round up
    • exponentiation
    • logarithm
    • square root
    • absolute value
c. ask the user for an integer value (positive, zero or negative)
d. display the following calculation table:
    Entered value: xxx
    # Calculations #
    - Absolute value: xxx
    - Squared: xxx
    - Cube: xxx
    - Square root: xxx
    - Natural logarithm: xxx
    - Base 10 logarithm: xxx
"""


import math

def display_math_content():
    print("\nThe contents of the math module:")
    for i in dir(math):
        print(f"\t{i}")


def display_functions_help():
    print("\n\n\nHelp of some functions are given below:")
    some_functions = [math.ceil, math.pow, math.log, math.sqrt, math.fabs]
    for i in some_functions:
        help(i)


def user_input():
    input_ = input("Enter an integer number: ")
    try:
        input_ = int(input_)
        return input_
    except:
        print("Invalid Integer! Cannot be calculated")
        quit()


def calculation_table(num):
    function_list = [math.fabs(num), math.pow(num, 2), math.pow(num, 3), math.sqrt(num), math.log(num), math.log10(num)]
    function_name_list = ["- Absolute value:", "- Squared:", "- Cube:", "- Square root:", "- Natural logarithm:", "- Base 10 logarithm:"]
    print("# Calculations #")
    for a, b in zip(function_name_list, function_list):
        print("{:<30}{:<30}".format(a,b))

def main():
    display_math_content()
    display_functions_help()

    print("\n\n\n")
    user_in = user_input()

    print("\n\n\n")
    calculation_table(user_in)

if __name__ == "__main__":
    main()