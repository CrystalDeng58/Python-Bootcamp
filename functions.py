print("This code returns the largest number from a list of user-input numbers.\n")

numbers = []

def getNumbers():
    while True:
        userInput = input("Enter a number or enter 'quit'. \n")
        if userInput == "quit":
            break
        else:
            userInput = int(userInput)
        numbers.append(userInput)
    return numbers

getNumbers()
print(numbers,"\n")

def maximumNumber(list):
    maximumNumber = max(list)
