# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

movieTicket = float(input("Enter your age"))
day = input("Enter the day").lower()

if movieTicket>=18:
    ticket=12
elif movieTicket<=18:
    ticket=8
else:
    print("Enter proper choice!")

if day=="wed":
    ticket-=2
    print(f"you got discount of {ticket} ")
else:
    print("Enter proper choice!")