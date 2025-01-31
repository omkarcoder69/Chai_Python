chai_types = {"massala" : "spicy" , "ginger" : "zesty"}

print(chai_types["ginger"])
print(chai_types)

for  i in chai_types:
    print(i,chai_types[i])

if "massala" in chai_types:
    print("massala data is exist")
else:
    print("massala does not exist")

print(len(chai_types))

chai_types["choclate"] = "coffee"

print(chai_types)

print("----")
chai_types.popitem()
# chai_types.pop("choclate")

print(chai_types)

del chai_types["ginger"]
print(chai_types)

tea_shop = {
    "chai":{
        "massala":"medium",
        "ginger":"zesty"
    },
    "tea":{
        "green":"mild",
        "black":"strong"
    }

}
print(tea_shop)

square_no = {
    x:x**2 for x in range(10)
}

print(square_no)

square_no.clear()

print(square_no)

keys = {1,2,3,4}

default_value = "delcious"
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)