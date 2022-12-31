"""
Write a program to determine whether an employee is owed any overtime. You should ask the
user how many hours the employee worked in a specific week, as well as the hourly wage for this
employee. If the employee worked more than 40 hours, you should print a message which says the
employee is due some additional pay, as well as the amount due. The additional amount owed is 20%
of the employees” hourly wage for each hour worked over the 40 hours.
"""

hours_worked = int(input("How many hours did you work in a week? "))
hourly_wage = int(input("What is your hourly wage? "))


if hours_worked > 40:
    overtime_hours = hours_worked - 40
    additional_wage = (0.2 * hourly_wage) * overtime_hours
    print(f"\nYou are due an additional pay of {additional_wage}!")