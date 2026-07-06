n = int(input("Enter a number:"))

sum = 0
i = 1

while i <= n: # Loop from 1 to n
    sum = sum+i
    i = i+1

print("The sum of numbers from 1 to", n, "is:", sum)