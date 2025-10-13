# Write a program to calculate the mean of elements in a tuple of integers.

numbers_list = [int(i) for i in input("Enter numbers separated by commas: ").split(',')]

numbers_tuple = tuple(numbers_list)
print("Tuple:", numbers_tuple)

print("Mean of the tuple:", sum(numbers_tuple) / len(numbers_tuple))
