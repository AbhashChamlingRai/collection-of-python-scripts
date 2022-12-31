#1) Roots of a Quadratic Equation

import math #importing maths for using sqrt method

#The variables(user inputs) A, B, C, root1 and root2 are type -> float
A = float(input("Enter a number: "))
B = float(input("Enter another number: "))
C = float(input("Enter last number: "))
print("\n")

print(f"Your values are: {A}, {B} & {C}\n")

d = math.sqrt(B*B-4*A*C)

root1 = (-B+d)/(2*A)
root2 = (-B-d)/(2*A)

print(f"The two root values are: {root1} & {root2}\n")
quit()



# Testing case 1 (passed):
#     A = 1, B = 0, C = -4
#     Root 1 = 2.0 (should be 2.0)
#     Root 2 = -2.0 (should be -2.0)

# Calculating case 2:
#     A = 1, B = 5, C = -36
#     Root 1 = 4.0
#     Root 2 = -9.0

# Calculating case 3:
#     A = 2, B = 7.5, C = 6
#     Root 1 = -1.1569296691827464
#     Root 2 = -2.5930703308172536

# Calculating case 3:
#     A = 0, B = 3.5, C = 8 # this test case fails and generates an error (why?):
#
#     Python throws ZeroDivisionError while calculating root1 (line 15);
#           ZeroDivisionError: float division by zero
#     This error occurs because the value ofuser given A which is the first number is zero. In the formula for finding root1(line 15) and root2(line 16), "A" is in the denominator which results in the value of the roots being infinite.