num = int(input("Enter a number: "))

num = str(num)
num_len = len(num)
num_dig = 0
i = 1

while num_dig < num_len:
    num_dig = num_dig + 1

print("The number of digits in the number is:", num_dig)
