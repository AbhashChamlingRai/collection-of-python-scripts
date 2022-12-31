"""
5.4 Write a function named sum(list_x, list_y) that expects two lists of numbers
and returns a new list containing the sums of those lists' members.
"""

def sum(list_x, list_y):
    '''
    Returns a new list containing the sums of two lists' corresponding members
    '''

    to_return = []

    for index, each in enumerate(list_x):
        inner_val = each + list_y[index]
        to_return.append(inner_val)
    
    return to_return
    
if __name__ == "__main__":
    print(sum([2,4,7], [1,2,3]))