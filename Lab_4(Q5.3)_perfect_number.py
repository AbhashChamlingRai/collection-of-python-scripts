"""
5.3 Write a Python function to check whether a number is perfect or not. (A perfect number is a positive
integer that is equal to the sum of its proper positive divisors ex. 28 = 1 + 2 + 4 + 7 + 14)
"""

def perfect_number_checker(num):
    try: #checking to see if user gave valid integer input
        num = int(num)
    except: #If not then print error and terminate
        print("\nPlease enter a valid positive Integer!")
        quit()
    
    if num < 0: # In case number is negative; print error and terminate
        print("\nPlease enter a valid positive Integer!")
        quit()

    total = 1 #sum of num's proper positive divisors
    for i in range(2, num):
        if num % i == 0:
            total += i
    


    if total == num:
        print("\nThe number is a perfect number!")
    else:
        print("\nThe number is not a perfect number!")

def main():
    user_in = input("\nEnter a number to check if its a perfect number: ")
    perfect_number_checker(user_in)

main()