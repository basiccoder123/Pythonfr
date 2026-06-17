print("Enter your marks for the following 4 subjects.")

math = int(input("Marks for math:"))
science = int(input("Marks for science:"))
french = int(input("Marks for french:"))
english = int(input("Marks for english:"))

total = math+science+french+english
print("The total marks are:", total)

total /= 400
print("Print the average is:", total)

avg = total*400

perc = (avg/400)*100
print("The percentage is:", perc)