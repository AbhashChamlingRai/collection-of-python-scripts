"""
This python file shows :

    - how to declare types to function's parameters

    - and, how to assert a condition in a function or methods.

    - Also, how to print error messages with full tracebacks without terminating the program
    
"""

#creating a error traceback printer which prints error message without terminating the program
import traceback
def traceback_printer():
    traceback_str = traceback.format_exc()
    print(traceback_str)




# 1 - Creating a normal function:
def for_integers1(p):
    print(p)
for_integers1(1)


# 2 - Performing (parameter) type declaration:
def for_integers2(p: int):
    print(p)
for_integers2(2)
for_integers2("2") # We have declared in function 'for_integers2', int value is required for 'p' parameter, but no error will be thrown unless assertion is used.


# 3 - Then, performing (return) type declaration:
def for_integers3(p: int) -> str:
    print(p)
    return str(p)
for_integers3(3) # The returned value is of type string and it is indicated in the line 34 after '->'. But, returning other types values won't throw error.


# 4 - Finally, performing single assertion:
def for_integers4(p: int) -> str:
    # assert <condition>, <optional error message>
    assert p > 0, "Positive integer value is required" # checking if passed value is positive
    print(p)
    return str(p)
try:
    for_integers4(-2) # Should throw error because negative integer is passed
except Exception as e:
    traceback_printer()


# 5 - Finally, performing single assertion:
def for_integers4(p: int) -> str:
    # assert <condition>, <optional error message>
    assert type(p) is int, f"Value of type int is required, but type {type(p)} is given." # Check if passed value is integer; should be kep at first
    assert p > 0, "Positive integer value is required"
    print(p)
    return str(p)
try:
    for_integers4("12uu") # Should throw error because integer is passed
except Exception as e:
    traceback_printer()


"""
Why use assertion?

- assert is a keyword in Python that is used to test if a given condition is True. 
- If the condition is True, the program will continue to execute the next line of code, 
- but if the condition is False, the program will raise an AssertionError with an optional error message.
"""