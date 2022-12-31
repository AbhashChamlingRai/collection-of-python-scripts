# 5.7 Write a Python program to compute Fibonacci series.


# define a function to calculate the nth number in the Fibonacci series
def fibonacci(i):
    # if i is less than or equal to 0, return 0
    if i <= 0:
        return 0
    # if i is 1, return 1
    elif i == 1:
        return 1
    # otherwise, use the formula to calculate the nth number
    else:
        return fibonacci(i-1) + fibonacci(i-2)

# prompt the user to enter the nth number in the series
user_input = input("\nEnter the nth number you want to find value of in Fibonacci series: ")

# if the user input is a valid number, calculate the nth number
if user_input.isdigit() == True:
    # convert the user input to an integer
    user_input = int(user_input)
    # calculate the nth number in the Fibonacci series
    nth_number = fibonacci(user_input)

    # print the result
    if nth_number == 0:
        print(f"\n{nth_number} term is 0")
        print(f"Series: 0")
    elif nth_number == 1:
        print(f"\n1st term is 1")
        print(f"Series: 0 1")
    else:
        print(f"\nThe {user_input}th number in the Fibonacci series is {nth_number}.")
        print("\nSeries:")
        print("0 1 ", end="")
        series= [(fibonacci(i-1) + fibonacci(i-2)) for i in range(2, user_input+1)]
        for x in series:
            print(x, end=" ")
        print()

else:
    # if the user input is not a valid number, print an error message
    print("Enter a valid number!")