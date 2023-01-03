def create_list():
    """
    It returns a list with the following elements:
    ['Playstation', 'Xbox', 'Steam', '10S', 'Google Play']
    """
    return ['Playstation', 'Xbox', 'Steam', '10S', 'Google Play']


def get_info(my_list):
    '''
    It returns the following information of my_list as a tuple:
        the firs element, 
        the second last element, 
        number of elements.
    '''
    return my_list[0], my_list[-2], len(my_list)


def get_partial(my_list):
    '''
    It returns a new list which contains the 2nd, 3rd, and 4th elements from my_list, in the orignal order.
    '''
    return [my_list[1], my_list[2], my_list[3]]


def get_last_three(my_list):
    '''
    It returns a new list which contains the last three elements from my_list, in the reversed order.
    '''
    return [my_list[-3], my_list[-2], my_list[-1]]


def double_list(my_list):
    '''
    It returns a new list which concatenates two of my_list.\
    '''
    return my_list+my_list


def amend(my_list):
    '''
    It returns a new list which the following amendments:
    change the 2nd element of my_list to "None",
    add "Bye" to the end of my_ist.
    '''
    my_list[1] = None
    my_list.append("Bye")
    return my_list


if __name__ == "__main__":
    test_list = create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))