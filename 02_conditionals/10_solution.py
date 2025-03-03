# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).


petFood = input("Enter your pet food spices")
petAge = float(input("Enter your pet age"))

if petFood == "dog" and petAge<=2:
    print("puppy food")
elif petFood == "cat" and petAge>=5:
    print("senior cat food")
else:
    print("enter proper choice")
