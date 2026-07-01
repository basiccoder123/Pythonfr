med_cause = input("Did you have a medical cause for your absence? (Y/N): ").strip().upper()


if med_cause != "y" or "Y" or "n" or "N":
        print("You must enter a valid input.")

elif med_cause == "Y":
    print("You are eligible for the exam.")

else:
    atten = int(input("Enter the amount of classes you have attended: "))
    if atten >= 75 and atten <= 100:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")