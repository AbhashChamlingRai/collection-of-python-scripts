"""
5.1 Create a function named print_full_pyramid(level, symbol), which takes two parameters: level and
symbol.
    • level: an integer and it's greater than 0.
    • symbol: a string to form the pyramid.
"""


def print_element_index_pyramid(level):
    '''
    This function gives a nested list of indexes to print out in a pyramid design
    For example:
        For print_element_index_pyramid(6):
        [[6], [5, 7], [4, 6, 8], [3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9, 11]]
    '''
    final_list = [[level]]
    
    while True:
        in_list = final_list[-1]
        next_level = []
        for num, i in enumerate(in_list):
            if num+1 != len(in_list):
                next_level.append(i-1)
            else:
                next_level.append(i-1)
                next_level.append(i+1)
        if next_level[-1] != (level+level-1):
            final_list.append(next_level)
        else:
            final_list.append(next_level)
            break
    return final_list





def print_full_pyramid(level, symbol):
    '''
    prints a pyramid shape of given level using the symbol provided as parameter in the function
    '''
    symbol = symbol.strip() # Getting rid ofany empty spaces in start or after end of the string
    gap_len = len(symbol) # Getting the length of symbol
    last_lvl = level + level -1

    elements_levels_indexes = print_element_index_pyramid(level)

    for i in elements_levels_indexes:
        for index_, each in enumerate(i):
            
            if each != i[-1]:
                if each == i[0]:
                    print(" "*gap_len*(each-1), end="")
                    print(symbol, end="")
                else:
                    print(" "*gap_len, end="")
                    print(symbol, end="")
            else:
                if each == last_lvl:
                    print(" "*gap_len, end="")
                    print(symbol)
                else:
                    if i == elements_levels_indexes[0]:
                        print(" "*gap_len*(each-1), end="")
                        print(symbol, end="")
                        print(" "*gap_len*(last_lvl-each-1), end="")
                        print(" "*gap_len)
                    else:
                        print(" "*gap_len, end="")
                        print(symbol, end="")
                        print(" "*gap_len*(last_lvl-each-1), end="")
                        print(" "*gap_len)


if __name__ == "__main__":
    print("\n6 Level pyramid with '*' symbol:")
    print_full_pyramid(6, "*")

    print("\n\n\n\n\n6 Level pyramid with '#' symbol:")
    print_full_pyramid(6, "#")

    print("\n\n\n\n\n9 Level pyramid with 'Hi' symbol:")
    print_full_pyramid(9, "Hi")

    print("\n\n\n\n\n4 Level pyramid with 'It's hard' symbol:")
    print_full_pyramid(4, "It's hard")

    print("\n\n\n\n\n12 Level pyramid with '(*_*)' symbol:")
    print_full_pyramid(12, "(*_*)")