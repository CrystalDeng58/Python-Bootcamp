import random

print("I am thinking of an integer between 0 to 100.\n")

correct_num = random.randint(0, 100)
iter = 0

while True:
    iter = iter + 1
    guess = input("Enter your guess or enter 'quit'!\n")
    if guess == "quit":
        break
    try:
        guess = int(guess)
    except:
        print("Please enter an integer.\n")
        iter = iter - 1
        continue
    if guess < 0 or guess > 100:
        print("My number is between 0 and 100... don't be stupid!\n")
        iter = iter - 1
        continue
    else:
        guess = int(guess)
        if guess == correct_num:
            print("Correct!", guess, "is indeed my number.\n")
            print("You got this answer in", iter, "guesses.\n")
            break
        elif guess < correct_num:
            print("Your guess is too small.\n")
            continue
        elif guess > correct_num:
            print("Your guess is too large.\n")
            continue

print("\nNow try it yourself!")
