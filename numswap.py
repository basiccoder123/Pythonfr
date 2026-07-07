a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(f"Before swap: a = {a}, b = {b}, c = {c}")


temp = a
a = b
b = c
c = temp

print(f"After swap: a = {a}, b = {b}, c = {c}")
