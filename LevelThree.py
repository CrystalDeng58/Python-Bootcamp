import random

print("Level 3: 10 random questions with a scoring system.\n")

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
    oper = random.choice(operations)      # This function chooses a random element in the list.
    if oper == "add":
        print("Question", i + 1, ":", "What is", num1, "+", num2,"?")
        ans = num1 + num2
    elif oper == "substract":
        print("Question", i + 1, ":", "What is", num1, "-", num2,"?")
        ans = num1 - num2
    elif oper == "multiply":
        print("Question", i + 1, ":", "What is", num1, "*", num2,"?")
        ans = num1 * num2
    elif oper == "divide":
        print("Question", i + 1, ":", "What is", num1, "/", num2, "to one decimal place?")
        ans = round(num1 / num2, 1)
    guess = input()
    check = checkAnswer(guess, ans)
    score = score + scoring(check)
    print("Your current score is", score, ".\n")

print("Your final score is", score, ".")
