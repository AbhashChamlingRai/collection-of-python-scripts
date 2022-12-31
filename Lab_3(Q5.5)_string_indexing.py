# 5.5 Write a program that loads an integer and prints its second digit from the left, third digit from the right. The digits will be printed if the given number has three digits, otherwise a message should be printed.



#taking input from user
given_number = input("\nEnter a number with atleast 3 digits: ")

# check if the given number is a valid number with at least 3 digits
if given_number.isdigit() == True: #check if the number is all digits
    if len(given_number) >= 3: #check if the number has at least 3 digits
        # calculate the second digit from the left and third digit from the right
        second_digit_from_left = given_number[1] #positive string indexing
        third_digit_from_right = given_number[-3] #negative string indexing
        # print the result
        print(second_digit_from_left, third_digit_from_right)
    else:
        # if the number does not have at least 3 digits, print an error message
        print("\nPlease enter a number with 3 or more digits!")
else:
    # if the given number is not a valid number, print an error message
    print("\nPlease enter a valid number!")