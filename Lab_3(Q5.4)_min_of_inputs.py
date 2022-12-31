# 5.4 Write a program that accepts integer inputs from a user as long as the word stop is not input. Compute and print the minimum of these integers.

user_nums_db = [] #A list of all user inputs

while True:
    looped_input = input("Enter number: ")
    print("Enter 'stop' to terminate and find the minimum of all your numbers.\n")

    try: #using try except block to check if user input is a number in every loop
        looped_input = int(looped_input)
        

        if looped_input not in user_nums_db: #Add to list only if there are no other same value
            user_nums_db.append(looped_input)

    except: #if user input value other than integer like "stop", following will be run
        if looped_input.lower() == "stop": #checking whether the user intput is 'stop' whether it is in all capital or lower; it is lowercased while comparing
            print(f"---The minimum number of all the numbers you gave is {min(user_nums_db)}.")
            break
        else: #if the user input is not 'stop'
            print("***PLEASE ENTER A VALID NUMBER OR 'stop'***\n")
            continue

