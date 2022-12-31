"""
5.5. Write a function called word frequencies(list_a) that accepts a list of strings
called list_a and returns a dictionary where the keys are the words from list_a and the
values are the number of times that word appears in list_a.
"""


def word_frequencies(list_a):
    '''
    Rturns a dictionary where the keys are the words from list_a and the
    values are the number of times that word appears in list_a
    '''
    to_return = {}

    for each in list_a:
        if each not in to_return:
            to_return[each] = 1
        else:
            to_return[each] += 1
    
    return to_return

if __name__ == "__main__":
    print()
    print(word_frequencies("Abhash Rai"))