
# intentations
# # 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = float(input("Enter your age"))
if age<=13:
    print("Child")
elif age>=13 and age <=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior")