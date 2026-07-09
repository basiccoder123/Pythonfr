rowSize = int(input("enter the number of rows: "))
if rowSize%2==0: #conditions
  halfDiamRow = int(rowSize/2)
else:
  halfDiamRow = int(rowSize/2)+1

# blank spaces printed before each of the numbers in every row
space = halfDiamRow-1
#loop for upper part
# value of i in the outer loop
# each value of i represents a row
for i in range(1, halfDiamRow+1): #loop for rows
  for j in range(1, space+1): #loop for columns
    print(end=" ")
  space = space-1 # each new row shifts; before printing the numbers the spaces are going to be...
  num = 1 # restarting the number
  for j in range(2*i-1):
    print(end=str(num))
  #incerementing number at each column
    num = num+1
  print()
space = 1
#loop for lower part
for i in range(1, halfDiamRow): #loop for rows
  for j in range(1, space+1):  #loop for columns
    print(end=" ")
  space = space+1
  num = 1
  for j in range(1, 2*(halfDiamRow-i)):
    print(end=str(num)) #display result
  #incerementing number at each column
    num = num+1
  print()
