# Write a program to count the frequency of all the elements in a tuple.

numbers_list = [int(i) for i in input("Enter numbers separated by commas: ").split(',')]
numbers_tuple = tuple(numbers_list)

print("Tuple:", numbers_tuple)
print("\nFrequency of each element:")

for element in tuple(set(numbers_tuple)):
    print(element, "occurs", numbers_tuple.count(element), "times")
