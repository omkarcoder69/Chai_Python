# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

ripe = ["yellow"]
unripe = ["banana"]
overripe = ["brown"]             

fruitChecker  = input("Enter fruit checker").lower()

if fruitChecker == ripe[0]:
    print("ripe")
elif fruitChecker == unripe[0]:
    print("unripe")
elif fruitChecker == overripe[0]:
    print("overripe")
else:
    print("plz enter propert colour input")