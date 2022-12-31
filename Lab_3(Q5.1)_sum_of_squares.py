# 5.1 Write a loop that computes the sum of the squares of the numbers between 1 and 100, inclusive.

total = 0
for i in range(1, 101):
    total += i**2
print(f"\nThe sum of the squares of the numbers between 1 and 100, inclusive is {total}")

