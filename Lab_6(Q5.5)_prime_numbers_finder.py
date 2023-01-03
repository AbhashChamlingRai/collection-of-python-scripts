"""
5.5. Create in Python a program which receives a positive integer number from the user and displays the list
of prime numbers smaller than the given value. The program must follow these guidelines:

    a. it must manage the entry of invalid inputs
    b. even numbers should be excluded from the check, since they cannot be prime numbers

E.g., if the user enters number 10, the result must be: “Prime list: 1, 2, 3, 5, 7”.
"""

def valid_input_checker(dta):
    '''
    dta --> string dtype, should be raw input from user (no change in data type; must be string)

    Checks wether the function input "dta" is a valid positive integer.
    If not then, prints error and terminates program.
    '''
    if dta.isdigit() == True or "-" in dta: # if the string contains all digits or "-" characer in it
        try: # Trying to change into integer
            dta = int(dta) 
        except: # If try block is unccessful then this except block will be executed (else block will be skipped)
            print("\nPlease input a valid 'positive integer' only and not other characters!") # When input has "-" and characters other than integers (E.g: -abs)
            quit()
        else: # If try block is successful then only this block is executed (except block will be skipped)
            if dta < 0: 
                print("\nPlease input a valid 'positive integer' only and not integers less than 0!") # if the input integer is less than 0. (E.g: -12)
                exit()
            else:
                print("\nValid input! Proceeding...")
    else:
        print("\nPlease input a valid 'positive integer' only and not other characters!") # if the input has characters other than integers (E.g: haha, 1d2)
        quit()


def prime_numbers_finder(num):
    if type(num) == str:
        num = int(num)
        
    list_of_prime_numbers = []
    
    for each in range(1, num+1):
        if each % 2 == 0: # if it is even just skipping it
            continue
        else:
            root_of_each = each**(0.5) # finding square root of each
            root_of_each = int(root_of_each) # Getting just the value before the decimal (E.g: 5.123 --> 5)
            
            for i in range(2, root_of_each+1): # Dividing by every number from 2 to "root_of_each" (inclusive)
                if each % i == 0: #if "i" perfectly divides "each"
                    continue
            list_of_prime_numbers.append(each) # adding as prime number only if all above conditions are fulfilled

    return list_of_prime_numbers


if __name__ == "__main__":
    user_input = input("\nEnter a positive integer to find all prime numbers less than it: ")

    valid_input_checker(user_input) #Checking if input is valid positive integer only

    prime_nums = prime_numbers_finder(user_input) # finding prime numbers

    print(f"\nPrime numbers are: {prime_nums}")
    
