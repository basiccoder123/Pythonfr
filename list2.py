
L = [5, 2, 8, 1, 9, 3]
print("Original list:", L)

count = 0

for i in L:
    count += i

avg = count / len(L)

print("Total sum:", count)
print("Average:", avg)

L.sort()

print("Smallest element:", L[0])
print("Largest element:", L[-1])