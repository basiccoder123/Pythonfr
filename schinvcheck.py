items = ["notebook", "pencil", "backpack", "calculator"]
stock_counts = [12, 0, 5, 3]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full inventory:", inventory)

available_items = [item for item in items if inventory[item] > 0]
print("Available items:", available_items)

chosen_item = input("Enter the item you want to buy: ")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"Sorry, {chosen_item} is not available.")
    exit()

prices = [10, 2, 5, 17]
markup = int(input("Enter the markup amount: "))

marked_up_prices = list(map(lambda price: price + markup, prices))
print("Marked-up prices:", marked_up_prices)

selected_index = items.index(chosen_item)
selected_price = marked_up_prices[selected_index]
print(f"Price of {chosen_item}: {selected_price}")

inventory[chosen_item] -= 1
print("Inventory after this purchase:", inventory)

print("=== SCHOOL INVENTORY MANAGEMENT SYSTEM ===")
print("The item bought was:", chosen_item, "for", selected_price)
print("The final inventory is:", inventory)
print("=== END OF SCHOOL INVENTORY MANAGEMENT SYSTEM ===")









