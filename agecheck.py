age = (input("Enter your age:"))

age = str(age)

if len(age) <= 2 :
    age = int(age)
    if age >= 10 and  age <= 20:
        print("You are at the required age.")
    
    else:
        print("You are not at the required age.")
else:
    print("Enter a valid age.")

