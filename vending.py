def calculate_change(paid, price):
    change = paid-price
    return change

snack_price = 25

print("Snack Vending machine")
print(f"This snack costs {snack_price} units")
print("Acceted coins include 10p, 20p, 50p")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin:"))
    
    if coin != 10 and coin != 20 and coin != 50:
        print("invalid coin")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    if total_inserted >= snack_price:
        print("Enought money inserted!\n")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing Snack")

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

