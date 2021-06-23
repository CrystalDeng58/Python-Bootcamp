import random

print("Level 1: Asks the user to add two values and tells them if their answer is correct.\n")

# This function adds two numbers.
def add(a, b):
    return a + b

# This function checks whether the user's answer is correct.
def checkAnswer(userInput, answer):
    if int(userInput) == int(answer):
        print("You are correct!\n")
    else:
        print("That's wrong.", answer, "is the correct answer.\n")

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sum = add(num1, num2)
    print("What is", num1, "+", num2,"?")
    guess = input()
    checkAnswer(guess, sum)
    exitGame = input("Do you want to keep playing? Enter 'yes' to continue and any other button to quit.\n")
    if exitGame == "yes":
        continue
    else:
        break

print("\nThanks for playing the game.")
