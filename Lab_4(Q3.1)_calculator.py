"""
3.1 Create a calculator program

Create a program that takes three parameters; two numbers and one string. The string is used to
indicate the arithmetic operation to apply on the two numbers. The program output should look
like the following:

input number 1: 7
input number 2: 5
Select an operator * for multiplication, - for subtraction, + for addition, / for division: *
Results: multiplying 7 by 5 = 35


4. The program must use an if statement that uses the sign operator string to decide on
the arithmetic operation to be done on the two numbers (See above example).

5. The program should returns the answer plus an explanation. For example, if the user
inputs 7, then 5 and then *, the program should return “multiplying 7 by 5 = 35”

6. The program should be able to call 4 functions to perform 4 arithmetic operations and
these are add, subtract, multiply and divide.

7. Then create a function calculator to implement the actual calculator.
"""



def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b


def calculator():
    '''Actual caculator function will be implemented here'''

    num1 = input("\nInput number 1 (Integer): ")
    try: #checking to see if user gave valid integer input
        num1 = int(num1)
    except: #If not then print error and terminate
        print("\nPlease enter a valid Integer!")
        quit()

    num2 = input("Input number 2 (Integer): ")
    try: #checking to see if user gave valid integer input
        num2 = int(num2)
    except: #If not then print error and terminate
        print("\nPlease enter a valid Integer!")
        quit()

    operator = input("Select an operator [* for multiplication, - for subtraction, + for addition, / for division]: ")
    # Checking if user gave valid input operator
    if len(operator) > 1 or operator not in ["*","+", "/", "-"]:
        print("\nPlease enter a valid operator!")
        quit()
    


    # Performing calculation according to user instructions
    if operator == "*":
        print(f"\nMultiplying {num1} by {num2} = {multiply(num1, num2)}")
    elif operator == "/":
        print(f"\nDividing {num1} by {num2} = {divide(num1, num2)}")
    elif operator == "-":
        print(f"\nSubtracting {num1} by {num2} = {subtract(num1, num2)}")
    elif operator == "+":
        print(f"\nAdding {num1} by {num2} = {add(num1, num2)}")


calculator()