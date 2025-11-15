# Write a program to create a list of random numbers using list comprehension.

import random

count = int(input("How many random numbers do you want? "))
start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))

random_list = [random.randint(start_range, end_range) for _ in range(count)]

print("Random list:", random_list)
