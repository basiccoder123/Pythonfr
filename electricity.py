print("Enter the amount of units of electricity consumed:", end="")
unit = int(input())

if unit <= 401: 
    if unit <= 50:
        amount = int(unit) * 2.00
        print("You are to pay:", amount)
        surcharge = 10
    elif unit <= 100:
        amount = int(unit) * 3.00
        print("You are to pay:", amount)
        surcharge = 15
    elif unit <= 200:
        amount = int(unit) * 4.00
        print("You are to pay:", amount)
        surcharge = 20
    elif unit <= 300:
        amount = int(unit) * 5.00
        print("You are to pay:", amount)
        surcharge = 25
    elif unit <= 400:
        amount = int(unit) * 6.00
        print("You are to pay:", amount)
        surcharge = 30
else:
    print("Visit the office for your bill.")