tea_variates = ["blacktea","greentea","oolang","white"]

print(tea_variates)

# indexing
print(tea_variates[1:3])
print(tea_variates[:3])
print(tea_variates[1:])

# how to change indexing
tea_variates[1]="coldtea"
print(tea_variates)

# tea_variates[1:2] = "lemon"
tea_variates[1:2] = ["lemon"]
# insert nothing 
# tea_variates[1:3] = []

print(tea_variates)

for i in tea_variates:
    print("---------")
    print(i)

# inbuilt method
tea_variates.append("oolang")
tea_variates.pop()
tea_variates.remove("oolang")
print(tea_variates)

if "oolang" in tea_variates:
    print("i have oolang tea")

tea_variates.insert(1,"green")
print(tea_variates)

#  same difference
tea_variates_copy = tea_variates
# different difference
tea_variates_copy = tea_variates.copy()

print(range(1,10))

square_no = [x**2 for x in range(10)]
square_no = [x+2 for x in range(10)]
print(square_no)

