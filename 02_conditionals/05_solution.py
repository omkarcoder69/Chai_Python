# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weatherCheck = {
    "sunny":"Go for a walk",
    "Rainy":"Read a book",
    "Snowy":"Build a snowman",

}

user = input("Enter  your weather suggestion:").lower()

if user in weatherCheck:
    print(f"Suggested activity is: {weatherCheck[user]}")
else:
    print("Enter proper choice")