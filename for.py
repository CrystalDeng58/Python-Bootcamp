# This code prints the first 5 even numbers.

# range takes in three parameters. (start, end, increment)
for i in range (0, 10, 2):
    print(i)

# x % y gives you the remainder when x is divided by y.

# continue moves the loop to the next iteration.
for i in range (10):
    if i % 2 == 0:
        print i
    else:
        continue
