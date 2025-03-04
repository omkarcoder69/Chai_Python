# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10,11,12]

positiveNumbercount = 0

for no in numbers:
    if no>0:
        positiveNumbercount+=1
print("list of positive numbers are",positiveNumbercount)


# Problem: Given a list of numbers, count how many are negative.
number = [1,2,3,4,5,-6,-7]

positiveNumbercoun = 0

for ns in number:
    if ns<0:
        positiveNumbercoun+=1
print("list of positive numbers are",positiveNumbercoun)