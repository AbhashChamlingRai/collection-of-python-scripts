"""
Write a Python program to determine whether a given year is a leap year based on the
given workflow for calculating a leap year.
"""

user_input_year = int(input("Enter a year: "))

if (user_input_year % 4 == 0):
    if (user_input_year % 100 == 0):
        if (user_input_year % 400 == 0):
            print("\nLeap year! Year %d is divisible by 4, 100 and 400." %user_input_year)
        else:
            print("\nNot leap year! year %d is divisible by 4 and 100, but not by 400." %user_input_year)
    else:
        print("\nLeap year! Year %d is divisible by 4 but not by 100." %user_input_year)
else:
    print("\nNot leap year! Year %d is not divisible by 4." %user_input_year)