# Write a program to find the mean, median, and standard deviation of a list of random numbers between 1 and 10.

import random
import statistics

n = int(input("Enter the number of random values to generate: "))
numbers = [random.randint(1, 10) for _ in range(n)]

print("Generated numbers:", numbers)

mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)
std_deviation = statistics.stdev(numbers)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
