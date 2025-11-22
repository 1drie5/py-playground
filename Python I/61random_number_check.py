# Write a program to generate a random number. Raise a user-defined exception if the number is below 0.5.

import random

class BelowThresholdError(Exception):
    """Custom exception for numbers below 0.5."""
    pass

number = random.random()
print("Generated number:", number)

try:
    if number < 0.5:
        raise BelowThresholdError("Number is below 0.5!")
    else:
        print("Number is acceptable.")
except BelowThresholdError as e:
    print(e)
