actcost = float(input("Enter the actual cost of the amount:"))
saleprice = float(input("Enter the selling price:"))

if actcost > saleprice:
    print("There is no profit!!")
else :
    amount = saleprice - actcost
    print("Total profit is {0}".format(amount))