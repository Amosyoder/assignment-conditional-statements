'''
Objective:
Harness the power of conditional statements to compare and determine values.
'''


# Task 1: Identify the Greatest number

num1 = float(input("Enter the first number; "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number:"))

largest_number = max(num1, num2, num3)
print("The largest number among the three is:", largest_number)

# Task 2: Extend the code to also identify the smallest number
smallest_number = min(num1, num2, num3)
print("The smallest number among the three is:", smallest_number)

# Task 3: Equality Check: check to see if two or more numbers are equal
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2 == largest_number or num1 == num3 == largest_number or num2 == num3 == largest_number:
    print("Two numbers are equal and the largest.")
elif num1 == num2 == smallest_number or num1 == num3 == smallest_number or num2 == num3 == smallest_number:
    print("Two numbers are equal and the smallest.")
