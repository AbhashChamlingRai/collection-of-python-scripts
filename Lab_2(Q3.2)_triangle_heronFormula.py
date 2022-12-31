"""
Write a python function to check whether three given numbers can form the sides of a
triangle. If the numbers can form the side of the tringle calculate the perimeter and the surface area
using Heron's Formula.
"""

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter last number: "))


if (a+b>c and a+c>b and b+c>a):
    perimeter = a + b + c

    s = perimeter / 2
    area = (s*(s-a)*(s-b)*(s-c))**0.5

    print("\nYour given numbers form a triangle!")
    print("Perimeter is %f" %perimeter)
    print("Area is %f" %area)
else:
    print("\nYour given numbers cannot form a triangle!")