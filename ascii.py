
for invalid in range(1, 6): #gives a certain amount of tries to input a valid character
    print("Invalid input. Please enter a single character.")
    char = input("Enter a single character:")
    if len(char) == 1 and isinstance(char, str): #checks if its a string and only 1 input is made
        print("Valid input")
        break

ascii_val = ord(char)

if ascii_val >= 65 and ascii_val <= 90: 
    print("You entered an uppercase letter and the ascii value of the letter is:",ascii_val)
elif ascii_val >= 97 and ascii_val <= 122:
    print("You entered a lowercase letter and the ascii value of the letter is:", ascii_val)

