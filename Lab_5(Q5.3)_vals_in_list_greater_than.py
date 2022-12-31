"""
5.3 Write a function named find_greater(x_list, x_num) that expects a list of
numbers and a number. It returns a new list consisting of all the numbers in the list
that are greater than the number x_num.
"""


def find_greater(x_list, x_num):
    '''
    returns a new list consisting of all the numbers in the list (x_list)
    that are greater than the number (x_num)
    '''
    to_return = []
    for each in x_list:
        if each > x_num:
            to_return.append(each)
    
    return to_return

if __name__ == "__main__":
    print(find_greater( [11, 35, 46, 2, 104, 43, 41,8], 10 ))