# Write a program to shuffle elements of a list of random numbers between given ranges.

import random

def generate_random_list(start_range, end_range, count):
    """Return a list of random numbers within the given range."""
    return [random.randint(start_range, end_range) for _ in range(count)]

def shuffle_list(numbers):
    """Shuffle the list elements in place."""
    random.shuffle(numbers)
    return numbers

start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))
count = int(input("Enter how many random numbers to generate: "))

random_list = generate_random_list(start_range, end_range, count)
print("Original list:", random_list)

shuffled_list = shuffle_list(random_list)
print("Shuffled list:", shuffled_list)
