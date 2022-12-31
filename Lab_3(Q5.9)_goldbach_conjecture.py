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








# 5.9 Extend Exercise 3.1. The Goldbach conjecture asserts that every even number is the sum of two
# prime numbers. Modify the program written in 3.1 that gets a number from the user, checks to
# make sure that it is even, and then finds two prime numbers that add up to it.


# prompt the user to enter a number
user_input = input("\nEnter an even number to find prime number whose sum equal to it: ")
print()


# check if the user input is a valid number
if user_input.isdigit() == True:
	# convert the user input to an integer
	user_input = int(user_input)

	# Initializing a list to keep all prime numbers less than the user input
	prime_nums_list = [1]

	# Checing if the number is even
	if user_input % 2 == 0:

		# checking if each number in the range is a prime number
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

			# if the current number is a prime number, add it to the list
			if is_prime_num == True:
				prime_nums_list.append(i)

		# Finding combination of prime numbersin "prime_nums_list" whose sum results to the user input
		sum_possible_prime_numbers = []
		
		for each_outer in prime_nums_list:
			for each_inner in prime_nums_list:
				if each_outer+each_inner == user_input and each_outer not in sum_possible_prime_numbers and each_inner not in sum_possible_prime_numbers:
					print(f"Sum of prime numbers {each_outer} and {each_inner} will give {user_input}.")
		

	else:
		print("\nThe number is not a even number!")

else:
	# if the user input is not a valid number, print an error message
	print("\nPlease enter a number!")
