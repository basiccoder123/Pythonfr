print("Enter a letter:", end="")
letter = input()

if  len(letter)!=1:
    print("You must enter a single letter.")
elif not isinstance(letter, str): #checks if its a string or not
    print("You must enter a letter.")
elif letter.isalpha() == True: #checks if its an alphabet or not
    print("You entered a letter.")
else:
    print("No letter detected.")
