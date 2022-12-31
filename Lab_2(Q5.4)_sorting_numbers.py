# Write a program that print three given numbers sorted from smallest to largest.
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter last number: "))
print()
user_inputs = [a,b,c]
user_inputs_sorted = []
for i in user_inputs:
    if len(user_inputs_sorted) == 0:
        user_inputs_sorted.append(i)
    elif len(user_inputs_sorted) == 1:
        if user_inputs_sorted[0] > i:
            user_inputs_sorted.insert(0, i)
        else:
            user_inputs_sorted.append(i)
    elif len(user_inputs_sorted) == 2:
        if i < user_inputs_sorted[0]:
            user_inputs_sorted.insert(0, i)
        elif i > user_inputs_sorted[1]:
            user_inputs_sorted.append(i)
        else:
            user_inputs_sorted.insert(1, i)
print(f"Your number sorted from smallest to largest: {user_inputs_sorted[0]}, {user_inputs_sorted[1]}, {user_inputs_sorted[2]}")