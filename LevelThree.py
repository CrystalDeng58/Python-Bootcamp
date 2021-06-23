import random

print("Level 3: 10 random questions with a scoring system.\n")

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

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

# Creates a list of operations to choose from.
operations = ["add", "substract", "multiply", "divide"]

score = 0
check = 0

for i in range(10):
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    random.shuffle(operations)      # This function shuffles up a list. 
    if operations[0] == "add":      # operations[0] refers to the first element of the operations list.
        print("Question", i + 1, ":", "What is", num1, "+", num2,"?")
        sum = add(num1, num2)
    elif operations[0] == "substract":
        print("Question", i + 1, ":", "What is", num1, "-", num2,"?")
        sum = substract(num1, num2)
    elif operations[0] == "multiply":
        print("Question", i + 1, ":", "What is", num1, "*", num2,"?")
        sum = multiply(num1, num2)
    elif operations[0] == "divide":
        print("Question", i + 1, ":", "What is", num1, "/", num2,"?")
        sum = divide(num1, num2)
    guess = input()
    check = checkAnswer(guess, sum)
    score = score + scoring(check)
    print("Your current score is", score, ".\n")

print("Your final score is", score, ".")
