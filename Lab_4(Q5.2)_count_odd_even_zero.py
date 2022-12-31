"""
5.2 Write a function named digits that takes one parameter that is a number (int) and returns a count of
even digits, a count of odd digits and a count of zero digit. For example: digit (1234567890123) returns
(5, 7, 1)
"""

def digit(num):
    '''
    Parameter: 
        Takes an integer number of multiple digits.

    Returns:
        1. count of even digits, 
        2. count of odd digits, 
        3. count of zero digit
    '''

    try: #checking to see if user gave valid integer input
        int(num)
    except: #If not then print error and terminate
        print("\nPlease enter a valid Integer!")
        quit()


    count_even = 0
    count_odd = 0
    count_zero = 0

    num = str(num) #Keeping the paramater num is still string so as to iterate later on 
    for i in num:
        if i == "0":
            count_zero += 1
        elif int(i) % 2 == 0:
            count_even += 1
        elif int(i) % 2 == 1:
            count_odd += 1
    
    return (count_even, count_odd, count_zero)


print(digit(1234567890123))
even, odd, zero = digit(1234567890123)
print(f"Even count: {even}, Odd count: {odd}, Zero count: {zero}")