# string is inmutable
chai = "LEMONCHAI"


slice_chai = chai[0:6]

# inbuilt method
print(slice_chai)
print(chai.lower())
print(chai.upper())

num_list = "01234567890"

# slicing
print(num_list[:])
print(num_list[2:4])
print(num_list[0:7:2])

chai = "Lemon Chai"
print(chai.replace("lemon" , "choclate"))


chai = "Lemon , ginger , massla , mint"
print(chai.split())
print(chai.split(" ,"))

name = "omkar"
print(name.find("om"))
print(chai.count("omkar"))

chai_type = "Massala"
quantiy = 2

order = f"i ordered {chai_type} cups of {quantiy} chai "
print(order)
print(order.format(quantiy,order))


# list

chai_variety = ["lemon" , "massala" , "ginger"]

print(" , ".join(chai_variety))

print(len(chai_variety))

chai  = "Hello said , \"massala dosa is awesome\" "
print(chai)

chai = r"c:/user/omkar/amazon"
print(chai)