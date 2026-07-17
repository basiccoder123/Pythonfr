# Simple Python Calculator with Repeat Option

def calculator():
    """Performs basic arithmetic operations."""
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Main loop to repeat the calculator
while True:
    calculator()
    choice = input("Do you want to calculate again? (y/n): ").strip().lower()
    if choice != 'y':
        print("Goodbye!")
        break
