import random

print("Level 2: 10 addition questions with a scoring system.\n")

# This function adds two numbers.
def add(a, b):
    return a + b

# This function checks whether the user's answer is correct.
def checkAnswer(userInput, answer):
    if int(userInput) == int(answer):
        print("You are correct!\n")
        return 1    # "1" represents that the user got the correct answer.
    else:
        print("That's wrong.", answer, "is the correct answer.\n")
        return 0    # "0" represents that the user was wrong.

# This function is the scoring system.
def scoring(check):
    if check == 1:  # Meaning the user is correct
        return 2
    else:           # Meaning the user is incorret
        return -1

score = 0
check = 0

for i in range(10):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sum = add(num1, num2)
    print("Question", i + 1, ":", "What is", num1, "+", num2,"?")
    guess = input()
    check = checkAnswer(guess, sum)
    score = score + scoring(check)
    print("Your current score is", score, ".\n")

print("Your final score is", score, ".")
