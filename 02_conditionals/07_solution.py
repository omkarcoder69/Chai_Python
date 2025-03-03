# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffeeOrder = {
    "coffeeSize":[
       "small" , "medium" ,"large" ],
    "extrashot":["true","false" ]  
}

coffeeSize = input("Enter the size of the coffee (small/medium/large)").lower()
coffeeShot = input("Enter do u want extra shot in coffee (true/false)").lower()

if coffeeSize in coffeeOrder["coffeeSize"]:
    if coffeeShot in coffeeOrder["extrashot"]:
        print(f"your customize is {coffeeSize} order and the extra shot is {coffeeShot} ")
    else:
        print("Enter proper coffee order")
else:
    print("coffee is not available")