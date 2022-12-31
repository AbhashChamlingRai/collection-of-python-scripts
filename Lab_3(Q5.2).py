"""
5.2 Use a single for loop to display a rectangle of asterisks with a given height and a given width.

            *****************
            *               *
            *               *
            *               *
            *****************
"""


height = 5
width = 17

total_asterisks = height*width #Total number of asterisks

breakers = [] #list of numbers; will be used in loop to break "print" into next line







print("\nPrinting full area rectangle")
for i in range(1,20): #Adding breakers
    val = width*i
    if val < total_asterisks:
        breakers.append(val)
    else:
        break

for i in range(1, total_asterisks+1): #printing full area rectangle
    if i not in breakers:
        print("*",end="")
    elif i in breakers:
        print("*")







print("\n\n\nPrinting rectangle with hollow or empty inside.")
empty_print_indexes = [x for x in range(breakers[0]+1, breakers[3]+1)] #finding indexes which should be a blank space instead of asterisks
for i in breakers:
    if i in empty_print_indexes:
        empty_print_indexes.remove(i)
    if i+1 in empty_print_indexes:
        empty_print_indexes.remove(i+1)

for i in range(1, total_asterisks+1): #printing rectangle with hollow or empty inside 
    if i not in breakers and i not in empty_print_indexes:
        print("*",end="")
    elif i in empty_print_indexes:
        print(" ",end="")
    elif i in breakers:
        print("*")