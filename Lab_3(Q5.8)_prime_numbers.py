## Lab_3(Q3.1).py script is below as comment
"""
3.1 A positive whole number n > 2 is prime if no number between 2 and √n (inclusive) evenly
divides n. Write a program that accepts a value of n as input and determines if the number is
prime. If n is not prime, your program should print all the divisors of n.

num = int(input("Enter a number to check wether it is a prime number: "))

root_val = int(num**0.5)

for i in range(2,root_val+1):
  if num%i == 0:
    print("\nNumber is not a prime number!")
    quit()
print("\nNumber is a prime number!")
"""





## 5.8 Extend Exercise 3.1(Lab 3). Modify your exercise 3.1 to

# prompt the user to enter a number
user_input = input("\nEnter a number to find prime number less than or equal to it: ")
print()

# check if the user input is a valid number
if user_input.isdigit() == True:
  # convert the user input to an integer
  user_input = int(user_input)

  # check if each number in the range is a prime number
  for i in range(2, user_input+1):
    # calculate the square root of the current number
    root_val = int(i**0.5)

    # assume that the current number is a prime number
    is_prime_num = True

    # check if the current number is divisible by any number in the range from 2 to the square root of the current number
    for x in range(2,root_val+1):
      if i%x == 0:
        # if the current number is divisible by any number in the range, it is not a prime number
        is_prime_num = False
        break

    # if the current number is a prime number, print it
    if is_prime_num == True:
      print(i, end=" ")

else:
  # if the user input is not a valid number, print an error message
  print("\nPlease enter a number!")


