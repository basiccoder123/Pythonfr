import random
secret = random.randint(1, 50)

def new_range(x, y):
ch_range = int(input("Chose starting range:"))
ch_range2 = int(input("Choose max range:"))
if ch_range >= ch_range2:
    temp = ch_range
    ch_range = ch_range2
    ch_range2 = temp

print(ch_range)
print(ch_range2)


for invalid in range(1, 5):
    print("You have", 5 - invalid, "guesses left.")
    guess = int(input("Guess a number between 1 and 50: "))
    if guess < secret:
        print("Your guess is too low.")
    elif guess > secret:
        print("Your guess is too high.")
    else:  
        print("Congratulations! You guessed the number.")
        break