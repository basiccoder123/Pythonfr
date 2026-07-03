n = int(input("Enter the number you want to find the sum of:"))
sum = 0

for i in range(1, n+1):
    sum += i
    print("\nSum is", sum)