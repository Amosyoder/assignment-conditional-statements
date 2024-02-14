
# Task 1: Leap Year Checker

year = int(input("Enter a year: "))
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
 
if is_leap_year:
     print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Task 2: Inform user if year entered is a century year, regardless if it's a leapyear
    
if year % 100 == 0:
    print(year, "is a century year.")

# Task 3: Indicate if the provided year is in the future or the past

current_year = 2024
if year > current_year:
    print(year, "is in the future.")
elif year < current_year:
    print(year, "is in the past.")
else:
    print(year, "is the current year.")