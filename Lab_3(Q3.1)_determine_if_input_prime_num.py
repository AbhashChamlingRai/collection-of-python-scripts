"""
3.1 A positive whole number n > 2 is prime if no number between 2 and √n (inclusive) evenly
divides n. Write a program that accepts a value of n as input and determines if the number is
prime. If n is not prime, your program should print all the divisors of n.
"""

num = int(input("Enter a number to check wether it is a prime number: "))

root_val = int(num**0.5)

for i in range(2,root_val+1):
    if num%i == 0:
        print("\nNumber is not a prime number!")
        quit()
print("\nNumber is a prime number!")
