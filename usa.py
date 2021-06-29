import matplotlib.pyplot as plt

# The code below checks how many words start with a certain letter.
file = open("usa.txt")  # The file must be in the same folder as the code.
count = 0
checkStart = input("Enter the letter you want to search.\n")
for lines in file:
    if lines.startswith(checkStart):
        count += 1
print("There are", count, "words that start with", checkStart, "\n")
file.close()


# The code below creates a bar graph with the starting letter frequency.
file = open("usa.txt")
i = 0
frequency = [0] * 26
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for lines in file:
    while i < 26:
        if lines.startswith(letters[i]):
            frequency[i] += 1
            break
        else:
            i += 1

# Creating the bar graph.
plt.bar(letters, frequency)
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.show()
