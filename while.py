# The while loop executes as long as a condition is met.

i = 1
while i <= 10:      # Sets the condition
    print(i)
    i += 1          # Updates the variable

print("\n\n")

# while True keeps running until "break"
j = 0
while True:
    print(j)
    j = j + 1
    if j > 10:
        break

print("\n\n")

# Counting down from 20 to 0.
x = 20
iter = 0            # Counts the number of iterations.
while True:
    iter += 1
    print(x)
    x -= 1          # Updates x. x = x - 1
    if x < 0:
        break
print("Finally done!\n")
print("We went through the loop", iter, "times.")
