# Test if a 5-digitnumber is a palindrome
a = input("Enter a number: ")
reversed = ""
length = len(a)

if length != 5:
    print("\nEnter a 5 digit number!")
    quit()

for i in range(0, len(a)):
    length -= 1
    reversed += a[length]

if a == reversed:
    print("Number is palindrome!")
else:
    print("Number is not palindrome!")