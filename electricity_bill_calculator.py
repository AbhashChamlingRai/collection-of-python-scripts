"""
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
            Unit                                                        Price
            First 100 units                                             no charge
            Next 100 units                                              Rs 5 per unit
            After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
"""

def bill_calculator(units):
    if units <= 100:
        print("\nNo charge!")
    elif units > 100 and units <= 200:
        remaining_unit = units-100
        remaining_unit_charge = remaining_unit * 5
        print(f"\nYour bill is: {remaining_unit_charge}")
    elif units > 200:
        first_200_units_price = 500

        remaining_units = units - 200
        remaining_units_price = remaining_units * 10

        total_bill = first_200_units_price + remaining_units_price

        print(f"\nYour bill is: {total_bill}")

if __name__ == "__main__":
    user_in = int(input("\nEnter electricity bill in units: "))
    bill_calculator(user_in)
    