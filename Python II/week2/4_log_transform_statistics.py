import random
import math
from statistics import mean, median, mode, stdev

# Generate 100 random numbers
numbers = [random.randint(1, 1000) for _ in range(100)]

# Apply logarithmic transformation
log_numbers = [math.log(x) for x in numbers]

# Statistics before transformation
print("Statistics before transformation:")
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Mean:", mean(numbers))
print("Median:", median(numbers))
print("Mode:", mode(numbers))
print("Standard Deviation:", stdev(numbers))

# Statistics after transformation
print("\nStatistics after transformation:")
print("Minimum:", min(log_numbers))
print("Maximum:", max(log_numbers))
print("Mean:", mean(log_numbers))
print("Median:", median(log_numbers))
print("Mode:", mode(log_numbers))
print("Standard Deviation:", stdev(log_numbers))
