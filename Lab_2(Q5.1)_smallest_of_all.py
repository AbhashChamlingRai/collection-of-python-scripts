#Find the smallest of three given numbers
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter last number: "))

if a < b and a < c:
    print(f"{a} is the smallest number")
elif b < a and b < c:
    print(f"{b} is the smallest number")
elif c < b and c < a:
    print(f"{c} is the smallest number")