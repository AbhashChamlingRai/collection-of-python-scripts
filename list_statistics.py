"""
Write a Python program that defines several functions to perform the following tasks:

    -Calculate the sum of all the items in a list
    -Count the number of items in a list
    -Calculate the average of all the items in a list
    -Find the minimum and maximum value in a list
"""

def sum_of_list(li):
    """
    This function takes a list as input and returns the sum of all the items in the list.
    """
    sum_ = 0
    for i in li:
        sum_ += i
    return sum_

def list_items_counter(li):
    """
    This function takes a list as input and returns the number of items in the list.
    """
    counter = 0
    for i in li:
        counter += 1
    return counter

def average_of_list_finder(li):
    """
    This function takes a list as input and returns the average of all the items in the list.
    """
    no_of_items_in_list = list_items_counter(li)
    sum_ = sum_of_list(li)
    average_ = sum_ / no_of_items_in_list
    return average_

def minimum_maximum_value_finder(li):
    """
    This function takes a list as input and returns the minimum and maximum value in the list as a tuple.
    """
    min_ = li[0]
    max_ = li[0]
    for i in li:
        if i < min_:
            min_ = i
        if i > max_:
            max_ = i
    return min_, max_

if __name__ == "__main__":
    list_ = [x for x in range(10, 50, 2)]

    print(f"\nList: {list_}")

    print(f"\nSum of the list: {sum_of_list(list_)}")

    print(f"Average of the list: {average_of_list_finder(list_)}")

    minimum_val, maximum_val = minimum_maximum_value_finder(list_)

    print(f"Smallest value: {minimum_val}")

    print(f"Largest value: {maximum_val}")
