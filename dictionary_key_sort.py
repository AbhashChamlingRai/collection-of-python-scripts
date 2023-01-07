"""
Write a Python function that takes a dictionary as an argument and returns a new dictionary with the same key-value pairs as the original, 
but with the keys sorted in alphabetical order. The function should not modify the original dictionary. 
The returned dictionary should maintain the association between each key and its corresponding value.
"""

def dictionary_sorter(dict_in):
    """
    Sorts a dictionary by its keys in alphabetical order and returns a new dictionary with the sorted key-value pairs.

    Parameters:
        dict_in (dict): The dictionary to be sorted.

    Returns:
        dict: A new dictionary with the sorted key-value pairs.
    """
    keys_list = list(dict_in.keys()) # Convert the dictionary's keys to a list
    sorted_keys_list = sorted(keys_list) # Sort the list of keys
    modified_dict = {} # Initialize an empty dictionary to store the sorted key-value pairs

    for each_key in sorted_keys_list:
        modified_dict[each_key] = dict_in[each_key] # Add the key-value pair to the modified dictionary
    
    return modified_dict

if __name__ == "__main__":
    to_sort = {
        'elephant': 5,
        'cat': 3,
        'dog': 4,
        'ant': 1,
        'horse': 8,
        'fish': 6,
        'bird': 2,
        'goat': 7,
        'iguana': 9,
        'jaguar': 10
    }

    # Call the function and store the returned dictionary
    sorted_dict = dictionary_sorter(to_sort)

    # Print the sorted key-value pairs
    print()
    for key_, val_ in sorted_dict.items():
        print('{:>10}:{:<5}'.format(key_, val_))
