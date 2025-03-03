# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

user = float(input("enter the leap year"))

if (user%4==0 and user%100!=0) or user%400==0:
    print(f"{user} is a leap year")
else:
    print(f"{user} is not a leap year")
