age = input("Age : ")
day = input("Day : ")
age_int = int(age)

price = 12 if age_int>=18 else 8

if day=="Wednesday":
    price = price-2
    # price-=2

print("Ticket Price is : $", price)