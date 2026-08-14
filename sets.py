basket1 = {"apple", "banana", "cherry", "mango","apple", 10}
basket2 = {"banana", "kiwi", "orange", "grape"}

print(f"Basket 1: {basket1}")
print(f"Basket 2: {basket2}")  

basket1.add("pear")
print(f"Basket 1 after adding pear: {basket1}")

common_fruits = basket1.intersection(basket2)
print(f"Common fruits in both baskets: {common_fruits}")

import array as arr
fruit_counts = arr.array('i', [5, 3, 8, 2, 7])
print(f"Fruit counts: {fruit_counts}")

fruit_counts.insert(2, 10)
fruit_counts.append(4)
print(f"Fruit counts after insertion and appending: {fruit_counts}")

count_of_5 = fruit_counts.count(5)
print(f"Count of apples (5) in fruit counts: {count_of_5}")

fruit_counts.reverse()
print(f"Fruit counts after reversal: {fruit_counts}")

print("")
print("===== CLASS FRUIT DESIGN COMPLETE =====")
print(f"Final Basket 1: {basket1}")
print(f"Final Basket 2: {basket2}")
print(f"Final Common Fruits: {common_fruits}")
print(f"Final Fruit Counts: {fruit_counts}")
print("===== END OF FRUIT DESIGN =====")