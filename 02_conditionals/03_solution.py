# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

student = float(input("Enter your grade in no"))

if student>=90 and student<=100:
    print("Student score A")
elif student>=80 and student<=89:
    print("Student score B")
elif student>=70 and student<=79:
    print("Student score C")
elif student>=60 and student<=69:
    print("Student score D")
else:
    print("Student score F")