"""
3.2 Write a menu-driven program that allows the user to make transactions to a bank account. The
options of the menu are:
    • Option 1: Make a Deposit
    • Option 2: Make a Withdrawal
    • Option 3: Obtain a Balance
    • Option 4: Quit

    a) First the program asks the user for his/her name.
    b) The user can make many interactions as they wish until they decide to quit by pressing Q or
    q from the keyboard. (Hint: while loop)
    c) Assume that the account initially has a balance of £1000.
    d) If the user tries to withdraw an amount more than the total balance, the program should print ‘It is
    not possible to withdraw beyond the account balance
    e) Ask the user to make a selection from the menu options.
    f) Make sure the user enters a proper menu number.
    g) If option one is selected, allow the addition of funds to the balance.
    h) If option two is selected, subtract the amount from the balance.
    i) If option three is selected, display the total balance of the checking account.
"""

import os

initial_balance = 1000
total_balance = initial_balance
user_name = input("\nPlease enter your name: ")

while True:
    print("\nPlease select your option (Enter the code):\n\t1: Make a Deposit\n\t2: Make a Withdrawal\n\t3: Obtain a Balance\n\t4: Quit")
    
    user_code = input("Enter desired code: ")

    if user_code not in ["1","2","3","4"] or user_code.isdigit() == False:
        print("\nPLEASE ENTER A VALID CODE!")
        input("\nPress Enter to continue...") #Awating user key press for allowing the user to read terminal texts


        #Clearing the terminal so as to keep the terminal clean
        if os.name =="nt": #windows
            os.system("cls")
        else:
            os.system("clear") #unix

    elif user_code == "1":
        try:
            deposit_amt = int(input("\nEnter deposit amount: "))
        except:
            print("\nEnter a valid number!")
            input("\nPress Enter to continue...")
            
            if os.name =="nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            if deposit_amt > 0:
                total_balance += deposit_amt
                print(f"\n--Your current balance now is £{total_balance}.")
                input("\nPress Enter to continue...")
                
                if os.name =="nt":
                    os.system("cls")
                else:
                    os.system("clear")
            else:
                print("\nIt is not possible to deposit negative amount.")
                input("\nPress Enter to continue...")
                
                if os.name =="nt":
                    os.system("cls")
                else:
                    os.system("clear")

    elif user_code == "2":
        withdrawl_amt = int(input("\nEnter withdrawl amount: "))
        if withdrawl_amt > total_balance:
            print("\nIt is not possible to withdraw beyond the account balance")
            input("\nPress Enter to continue...")
            
            if os.name =="nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            total_balance -= withdrawl_amt
            print(f"\n--Your current balance now is £{total_balance}.")
            input("\nPress Enter to continue...")
            
            if os.name =="nt":
                os.system("cls")
            else:
                os.system("clear")

    elif user_code == "3":
        print(f"\n--Your total balance is £{total_balance}.")
        input("\nPress Enter to continue...")
        
        if os.name =="nt":
            os.system("cls")
        else:
            os.system("clear")

    elif user_code == "4":
        break