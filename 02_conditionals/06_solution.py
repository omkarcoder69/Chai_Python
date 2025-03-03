# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).


userMode = float(input("Enter your mode of transportation"))

if userMode<=3:
    print("Mode of transportation Walk")
elif userMode>=3 and userMode<=15:
    print("Mode of transportation Bike")
elif userMode>=15:
    print("Mode of transportation Car")
else:
    print("Enter proper mode")