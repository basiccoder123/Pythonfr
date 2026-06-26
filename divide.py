print("Enter a number for numerator:", end="")
numn = int(input())

print("Enter a number for denominator:", end="")
numd = int(input())

if numn%numd == 0:
    print("It is divisible")
else:
    print("It is not divisible")
