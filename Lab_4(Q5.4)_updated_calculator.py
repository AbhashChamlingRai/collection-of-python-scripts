"""
5.4 Modify exercise Lab_4(Q3.1)_calculator.py:

1. create a function display_menu() which displays the following menu
    Select an option:
    1 Add
    2 Subtract
    3 Multiple
    4 Divide
    q Quit

2. Then create a function run_calculator() to implement the actual calculator.
    • This function uses display_menu() to display the menu.
    • It asks for user input to choose an option and acts accordingly:

        Choice                Action
        1/2/3/4:              Further asks user to enter two integer and prints out the results of the chosen operation.
        q:                    Print outs "Bye!".
        entered other choice: Print outs "Error: invalid choice.".
        
    o For division, it will display an error message when the divisor is 0.
    o For division, the result will be displayed with two decimal places
"""



def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def valid_number_receiver():
    '''
    This function asks user for two input and check if its a valid number before returning it
    '''
    num1 = input("\nEnter first number: ")
    try: #checking to see if user gave valid integer input
        num1 = float(num1)
    except: #If not then print error and terminate
        print("\nPlease enter a valid Integer!")
        quit()

    num2 = input("\nEnter second number: ")
    try: #checking to see if user gave valid integer input
        num2 = float(num2)
    except: #If not then print error and terminate
        print("\nPlease enter a valid Integer!")
        quit()
    
    return num1, num2
    

def display_menu():
    '''
    Prints menu option for performing calculations
    '''
    print("\nSelect an option:")
    print("\t1 Add")
    print("\t2 Subtract")
    print("\t3 Multiple")
    print("\t4 Divide")
    print("\tq Quit")


def run_calculator():
    display_menu()

    option_in = input("\nEnter you choice(1/2/3/4/q): ")

    if option_in not in ["1","2","3","4","q"]:
        print(f"You selected {option_in}.")
        print( "Error: invalid choice.")
        quit()
    elif option_in == "q":
        print(f"You selected {option_in}.")
        print("Bye!")
        quit()
    elif option_in == "1":
        print(f"You selected {option_in}.")
        a, b = valid_number_receiver()
        print(f"Result: {a} + {b} = {add(a,b)}")
    elif option_in == "2":
        print(f"You selected {option_in}.")
        a, b = valid_number_receiver()
        print(f"Result: {a} - {b} = {subtract(a,b)}")
    elif option_in == "3":
        print(f"You selected {option_in}.")
        a, b = valid_number_receiver()
        print(f"Result: {a} * {b} = {multiply(a,b)}")
    elif option_in == "4":
        print(f"You selected {option_in}.")
        a, b = valid_number_receiver()
        if b == float(0):
            print("Error: cannot divide by 0.")
            quit()
        else:
            print(f"Result: {a} / {b} = {round(divide(a,b), 2):.2f}")
        


if __name__ == "__main__":
    run_calculator()