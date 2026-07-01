print("Choose a ride.")
print("Bike")
print("Car")

choice = input("Enter your choice: ")

if choice == "Bike":
    print("Choose the type of bike you want to ride.")
    print("Mountain Bike")
    print("Road Bike") 
    choice_2 = input("Enter your choice: ")
    if choice_2 == "Mountain Bike":
        print("You have selected the mountain bike.")
    else:
        print("You have selected the road bike.")

elif choice == "Car":
    print("Choose the type of car you want to ride.")
    print("Urus")
    print("Yaris")
    choice_3 = input("Enter your choice: ")
    if choice_3 == "Urus":
        print("You have selected the Urus.")
    else:
        print("You have selected the Yaris.")
else:
    print("You have not selected a valid option.")