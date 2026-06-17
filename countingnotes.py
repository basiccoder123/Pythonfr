amount = int(input("Enter an amout for withdrawal:"))

note1 = amount//200
note2 = (amount%200)//100
note3 = ((amount%200)%100)//50
note4 = (((amount%200)%100)%50)//20
note5 = ((((amount&200)%100)%50)%20)//10
note6 = (((((amount&200)%100)%50)%20)%10)//5
note7 = ((((((amount&200)%100)%50)%20)%10)%5)//2
note8 = (((((((amount&200)%100)%50)%20)%10)%5)%2)//1

print("Amount of 200 cedis note:", note1)
print("Amount of 100 cedis note:", note2)
print("Amount of 50 cedis note:", note3)
print("Amount of 20 cedis note:", note4)
print("Amount of 10 cedis note:", note5)
print("Amount of 5 cedis note:", note6)
print("Amount of 2 cedis note:", note7)
print("Amount of 1 cedis note:", note8)
