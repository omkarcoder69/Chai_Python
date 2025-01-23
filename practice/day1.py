# program1:
name="omkar"
print(f"Hello {name} ")
print("Welcome to Python programming.")

# program2:

name = input("Enter your name")
age = float(input("Enter your age"))

print(f"your name is {name} and you are {age} years old ")


# program3:

no = float(input("Enter your number"))

if(no%2==0):
    print("number is even")
else:
    print("number is odd")

# program4: 

for i in range(1,11):
    print(i)


for i in range(1,51):
    if(i%2==0):
        print(i) 

# program5:

def sum2():
    n1 = float(input("Enter  number1:"))
    n2 = float(input("Enter number2:"))
    sum = n1 + n2
    return sum

print(sum2())

# program6:

fruits = ["apple","mango","banana","grapes","papaya"]

for i in fruits:
    print(i)


# program7:

userInfo = {
    "name":"alice",
    "age":25,
}

print(userInfo["age"])

# program8:

name = "omkar"

output=name[::-1]

print(output)

# program9:
# with open(day1.py,"r") as file:


# program10:
import math as m
num = float(input("enter square root "))
output= m.sqrt(num)
print(output)