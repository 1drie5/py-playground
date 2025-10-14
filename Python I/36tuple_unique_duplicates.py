# Write a program to display unique and duplicate elements of a tuple.

numbers_list = [int(i) for i in input("Enter numbers separated by commas: ").split(',')]
numbers_tuple = tuple(numbers_list)
print("Resultant Tuple:", numbers_tuple)

unique = []
duplicate = []

for element in numbers_tuple:
    if numbers_tuple.count(element) > 1:
        if element not in duplicate:
            duplicate.append(element)
    else:
        unique.append(element)

print("Unique Elements:", unique)
print("Duplicate Elements:", duplicate)
