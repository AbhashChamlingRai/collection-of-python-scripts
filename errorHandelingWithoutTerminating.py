"""
How to print error with full traceback as a string in python without terminating program
"""
import traceback

def traceback_printer(): #creating a error traceback printer which prints error message without terminating the program
    traceback_str = traceback.format_exc()
    print(traceback_str)

try: # Fot this purpose try Exceptmust be used
    print( "one" / 3) # creating a error condition
except:
    print()
    traceback_printer() # Calling our function to print error without terminating program

print("\nProgram is now terminated") # This should be printed