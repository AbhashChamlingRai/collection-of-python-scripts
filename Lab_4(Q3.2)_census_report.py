"""
3.2 Designing a program which generates housing occupancy report

1. In this task, you will design a program which display a census report of the numbers and percentages
of houses with particular numbers of occupants in a road.

2. When the program starts, it should ask the user 8 times about houses with occupancy of 0 to 6, plus 6+
to count the numbers of houses with particular numbers of occupants.
    • For each question, the user should enter a digit for the number of houses, e.g.:
    • Please note there is a space after the colon mark.
    • This step should be implemented in a function named get_data().
    • The function will return all the 8 integer values entered by the user.

3. After user entered the data, the program will calculate the percentage of each occupancy category.
    • For example, if the total house is 35 and the house with 0 occupant is 2, the percentage of
    houses with 0 occupancy is 5.7%. This is because (2/35) * 100 is 5.7%.
    • This step should be implemented in a function named cal_percentage().
    • The function should take 8 parameters of the house number for each occupancy category. The
    order of the parameters must be the same as the user entered in step 2.
    • The function will return 8 float values for percentages of each occupancy category in the same
order.

4. When the calculation finished, the program outputs the census result as below:
    • The output must comply with the width specification given above.
    • Read this article to find out more about setting format.
    • This step should be implemented in a function named display_result().
    • The function takes 16 parameters. The first 8 are for the house number of each occupancy
    category and second 8 are for the corresponding percentages.
    • The output of the function should follow the specification above.

5. To sum up, in the program, it should include definition of the three functions you have created and the
necessary codes to run the program
"""


def get_data():
    '''
    This function asks the user to input integer values for houses with particular numbers of occupants 8 times, stores it and returns it in the same order
    '''
    li = [] # Empty list to store user inputs in order
    for i in range(0, 8):
        if i != 7:
            curr = input(f"\nProvide the number of houses with {i} occupancy (Integer): ")
        elif i == 7:
            curr = input(f"\nProvide the number of houses with 6+ occupancy (Integer): ")
        
        try: #checking to see if user gave valid integer input
            curr = int(curr)
        except: #If not then print error and terminate
            print("\nPlease enter a valid Integer number!")
            quit()
        
        li.append(curr)
    
    return li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7]





def cal_percentage(a, b, c, d, e, f, g, h):
    '''
    Parameters -> This function takes 8 parameters  of the house number for each occupancy category
    Returns    -> It returns float values for percentages of each occupancy category in the same order as the parameter of this function
    '''
    
    in_li = [a, b, c, d, e, f, g, h] #Keeping in list to iterate over later
    percentage_li = [] # Empty list to keep float values for percentages

    total = sum(in_li) 

    for i in in_li:
        percentage = round((i/total)*100, 1)
        percentage_li.append(percentage)
    
    return percentage_li[0], percentage_li[1], percentage_li[2], percentage_li[3], percentage_li[4], percentage_li[5], percentage_li[6], percentage_li[7]





def display_result(a1,b1,c1,d1,e1,f1,g1,h1, a0,b0,c0,d0,e0,f0,g0,h0):
    '''
    Parameters ->   This function takes 16 parameters; 
                    First 8 are for the house number of each occupancy
                    Second 8 are for the corresponding percentages
                  
    Output    ->    Prints the the given parameters data in tabular form;
                    1st row: Occupants
                    2nd row: No. houses
                    3rd row: Percentages 
    '''

    print("\n\n\n")
    print("{:>12}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}".format("Occupants:", 0, 1, 2, 3, 4, 5, 6, ">6"))
    print("{:>12}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}".format("No. houses:", a1,b1,c1,d1,e1,f1,g1,h1))
    print("{:>12}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}{:>7}".format("Percentage:", f"{a0}%", f"{b0}%", f"{c0}%", f"{d0}%", f"{e0}%", f"{f0}%", f"{g0}%", f"{h0}%"))

    print("\n\n\n")




def main():
    '''This function will implement all the above functions to create the report'''

    a, b, c, d, e, f, g, h = get_data() # Getting 8 user data

    a0, b0, c0, d0, e0, f0, g0, h0 = cal_percentage(a, b, c, d, e, f, g, h) # Creating percentage number

    display_result(a, b, c, d, e, f, g, h, a0, b0, c0, d0, e0, f0, g0, h0) # Printing the report in tabular form


main()