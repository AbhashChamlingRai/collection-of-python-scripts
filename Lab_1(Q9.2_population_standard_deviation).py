# 2. Population standard deviation

# objective --> Write a Python script that calculates the sum, average and population standard deviation of 5 numbers stored in the variables a,b,c,d,e

import math

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))
e = float(input("Enter fifth number: "))
print()

sum = a + b + c + d + e #Finding the sum of every user given values

mean = sum / 5 #This is the mean value

user_inputs = [a,b,c,d,e] #storing user input in a list to iterate over the values
empty_var = 0 #This will store the sum of all subtracted value of mean from each data(a,b,c,d,e) which is also squared
for i in user_inputs:
    vvar = (i - mean)**2
    empty_var += vvar

variance = empty_var/5
standard_deviation = math.sqrt(variance)

print(f"The standard deviation is {standard_deviation}")
