import random
#import the random library

print("Level 2: 10 addition questions with a scoring system.\n")

score = 0
#define score, set it to 0

for i in range(10):
#for loop with iterator i, allows us to repeat the questions 10 times
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    #set the two numbers

    print("Question", i + 1, ":", "What is", num1, "+", num2,"?")
    #print the question
    ans = int(input())
    #set answer equal to user input

    if ans == num1 + num2:
    #if the user answers correctly
        print("Correct!")
        score = score + 2
        #tell the user that they're correct and increase score by 1

    else:
        print("Incorrect. The correct answer is", num1 + num2, ".")
        score = score - 1
        #tell the user that they're correct and increase score by 1

    print('Your current score is:', score, '\n')
    #print the user's current score after each question

print('\nYour final score is:', score, '\n')
#print the user's final score
