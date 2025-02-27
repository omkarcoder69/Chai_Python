# # 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# age = float(input("Enter your age"))


# if age<=13:
#     print("Child")
# elif age>=13 and age <=19:
#     print("Teenager")
# elif age>=20 and age<=59:
#     print("Adult")
# else:
#     print("Senior")

# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# student = float(input("Enter your grade in no"))

# if student>=90 and student<=100:
#     print("Student score A")
# elif student>=80 and student<=89:
#     print("Student score B")
# elif student>=70 and student<=79:
#     print("Student score C")
# elif student>=60 and student<=69:
#     print("Student score D")
# else:
#     print("Student score F")


# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

# ripe = ["yellow"]
# unripe = ["banana"]
# overripe = ["brown"]             

# fruitChecker  = input("Enter fruit checker").lower()

# if fruitChecker == ripe[0]:
#     print("ripe")
# elif fruitChecker == unripe[0]:
#     print("unripe")
# elif fruitChecker == overripe[0]:
#     print("overripe")
# else:
#     print("plz enter propert colour input")

# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# weatherCheck = {
#     "sunny":"Go for a walk",
#     "Rainy":"Read a book",
#     "Snowy":"Build a snowman",

# }

# user = input("Enter  your weather suggestion:").lower()

# if user in weatherCheck:
#     print(f"Suggested activity is: {weatherCheck[user]}")
# else:
#     print("Enter proper choice")


# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


# userMode = float(input("Enter your mode of transportation"))

# if userMode<=3:
#     print("Mode of transportation Walk")
# elif userMode>=3 and userMode<=15:
#     print("Mode of transportation Bike")
# elif userMode>=15:
#     print("Mode of transportation Car")
# else:
#     print("Enter proper mode")