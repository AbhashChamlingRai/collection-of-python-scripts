# 5.3 Write a loop that computes the sum of all the odd digits in a non-negative integer n.


sum = 0

try: #using try except block to check if user input is a number in the first place
    non_neg_int = int(input("Enter a non-negative integer: "))
    
    if non_neg_int < 0:
        print("\nPlease try again!")
    else:
        for i in range(1, non_neg_int+1):
            if i%2 == 1:
                sum += i
    print(f'\nThe sum of all the odd digits between 1 and {non_neg_int} is {sum}')

except: #if user input is nor a number then prompt user to try again
    print("\nPlease enter a number.")