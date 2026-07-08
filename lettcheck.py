string = input("Enter a word of your choice:")
char = input("Enter a character to check if it is present in the word:")

if len(char) != 1:
    print("Please enter a single character.")
    exit()

count = 0
i = 0

while (i < len(string)):
    if (string[i] == char):
        count += 1
    i += 1

print(f"The character '{char}' appears {count} times in the word '{string}'.")