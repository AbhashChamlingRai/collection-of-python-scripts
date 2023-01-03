"""
5.4 Create in Python the program containing the tuple: tuplex = (4, 9, ['a','b'], 123.45, 0)
At the end of the program the tuple must be changed in the following way, applying the changes in the exact
order given below (remember: tuples cannot be modified, they can only be reassigned, thus a list must be
used to perform the transition from the initial tuple to the final one):

    1. add value 7 at the end of the sequence
    2. add tuple (10, 100, 1000) in the fourth position
    3. add the string "bob" stored in the position with index 2
    4. add number 3.5 in first position
    5. add False in position -1
    6. delete value 9
    7. delete the element stored in the position with index -4

Display each change on the screen (printing each time the intermediate list) and, at last, print the final tuple
tuplex.
"""

def tuple_modifier(tuplex):
    print(f"\nInitial tuple: {tuplex}")

    tuplex = list(tuplex) #converting tuple into list
    print(f"\nConverted initial tuple into list: {tuplex}")

    tuplex.append(7)
    print(f"\nAdded value 7 at the end of the sequence: {tuplex}")

    tuplex.insert(3, (10, 100, 1000))
    print(f"\nAdded tuple (10, 100, 1000) in the fourth position: {tuplex}")

    tuplex.insert(2, "bob")
    print(f'\nAdded the string "bob" stored in the position with index 2: {tuplex}')

    tuplex.insert(0, 3.5)
    print(f'\nAdded number 3.5 in first position: {tuplex}')

    tuplex.insert(-1, False)
    print(f'\nAdded False in position -1: {tuplex}')

    tuplex.remove(9)
    print(f'\nDeleted value 9: {tuplex}')

    tuplex.pop(-4)
    print(f'\nDeleted the element stored in the position with index -4: {tuplex}')

    tuplex = tuple(tuplex)
    print(f"\nFinal tuple: {tuplex}")

if __name__ == "__main__":
    initial_tuple = (4, 9, ['a','b'], 123.45, 0)
    tuple_modifier(initial_tuple)
    
