# Check if a given number is of one digit or two digited or three digited or more than three digit
inn = input("\nEnter a number: ")

def digit_checker(in_digits):
    try:
        in_decimal = float(f"0.{in_digits}")
        
        in_digits = int(in_digits)
        # if int(inn):
        #     inn = int(inn)
        # else:
        
        if (in_digits / 10) == in_decimal:
            print("\nOne digit.")
        elif (in_digits / 100) == in_decimal:
            print("\ntwo digit.")
        elif (in_digits / 1000) == in_decimal:
            print("\nThree digit.")
        else:
            print("\nMore than three digits.")
    except:
        print("\nPlease type a number!")

if "-" not in inn and "." not in inn: #In case user gives a non negative number with no decimal
    # print("first")
    digit_checker(inn)

elif "-" in inn and "." not in inn: #In case user gives negative number with no decimal
    inn = inn[1:]

    digit_checker(inn)

elif "-" not in inn and "." in inn: #In case user gives non negative number with decimal
    inn = inn.replace(".", "")

    digit_checker(inn)

elif "-" in inn and "." in inn: #In case user gives a negative number with decimal
    inn = inn.replace(".", "")
    inn = inn[1:]

    digit_checker(inn)