"""
5.3 Create in Python the program containing a function, called report, which creates a
short report of the quantities of spare parts sold in three different stores (located in London, Birmingham
and Nottingham). The function:

    o receives three mandatory parameters (q1, q2 and q3) containing the quantities sold,
    respectively, in London, Birmingham and Nottingham.

    o receives three optional parameters containing the price of the spare parts: € 60 for spare parts
    sold in London, € 57 for those sold in Birmingham and € 59 for those sold in Nottingham.

    o calculates the revenue of each store, the average quantity sold and the average revenue.

    o create a report similar to the example shown below, showing two decimal digits for revenues
    and one decimal digit for the average quantity sold.


The main program must ask the user for the quantities sold in each store and call the report
function.
"""

def report(q1, q2, q3, price_London=60, price_Birmingham=57, price_Nottingham=59):
    cities = ["London", "Birmingham", "Nottingham"]
    quantities = [q1, q2, q3]
    each_prices = [price_London, price_Birmingham, price_Nottingham]
    revenue_list = []

    print("{:<20}{:<20}{:<20}{:<20}".format("Store", "Quantity", "Price", "Revenue[€]"))
    for city, quantity, per_price in zip(cities, quantities, each_prices):
        revenue = quantity*per_price
        revenue_list.append(revenue)
        print("{:<20}{:<20}{:<20}{:<20.2f}".format(city, quantity, per_price, revenue))
    
    quantity_mean = sum(quantities)/3
    price_mean = sum(each_prices)/3
    revenue_mean = sum(revenue_list)/3

    print("{:<20}{:<20.2f}{:<20.2f}{:<20.2f}".format("MEAN", quantity_mean, price_mean, revenue_mean))


if __name__ == "__main__":
    print()
    report(580,406,495)