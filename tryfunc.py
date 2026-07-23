try:
    num1, num2 = eval(input("Enter two numbers separated by a comma:"))
    result = num1/num2
    print(f"The Result is {result}")
except ZeroDivisionError:
    print("Number cannot be divided by zero")
except SyntaxError:
    print("Comma is missing from the numbers")
except:
    print("Wrong Input")
else:
    print("No errors or mistakes")
finally:
    print("This will run no matter what")