# Write a program to print random numbers infinitely. Raise the StopIteration exception after displaying 10 numbers to exit from the program.

import random
count = 0
while True:
    try:
        if count >= 10:
            raise StopIteration("Displayed 10 numbers. Exiting program.")
        number = random.randint(1, 100)
        print(f"Random number: {number}")
        count += 1
    except StopIteration as se:
        print(se)
        break
