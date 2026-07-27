import random
playing = True
number = int(random.randint(0,9))

print("I am going to produce a number from the range 0 to 9")
print("If you guess the number you win")

while playing:
    guess = int(input("Enter your guess:"))
    if guess == number:
        print("Congrats you guessed right")
        print(f"The number was indeed: {number}")
        break
    else:
        print("Oops you guessed wrong")
        continue