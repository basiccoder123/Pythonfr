science = int(input("Enter marks for science:"))
maths = int(input("Enter marks for maths:"))
eng = int(input("Enter marks for english:"))

tot = maths + eng + science

avg = int(tot/3)

validRange = range(0,101)

if (avg not in validRange):
    print("Invalid Input.")

elif avg in range(91,100):
    print("Grade A1")

elif avg in range(81,90):
    print("Grade A2")

elif avg in range(71,80):
    print("Grade B1")

elif avg in range(61, 70):
    print("Grade B2")