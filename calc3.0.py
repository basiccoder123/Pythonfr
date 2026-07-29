def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot be divided by zero")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

try:
  num_1 = float(input("Enter first number: "))
  num_2 = float(input("Enter second number: "))
except ValueError:
    print("Enter a number!!")

try:
 if choice == '1':
    print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
 elif choice == '2':
    print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
 elif choice == '3':
    print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
 elif choice == '4':
    print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")
 else:
    print("Invalid input. Please select a valid operation.")
except NameError:
   print("Not Defined!!")
          

