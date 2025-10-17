# Write a program to find the distinct pairs of numbers whose product is even from a tuple of integers.

numbers_list = [int(i) for i in input("Enter numbers separated by commas: ").split(',')]
numbers_tuple = tuple(numbers_list)
print("Resultant Tuple:", numbers_tuple)

even_product_pairs = []

for i in range(len(numbers_tuple)):
    for j in range(i + 1, len(numbers_tuple)):
        if (numbers_tuple[i] * numbers_tuple[j]) % 2 == 0:
            even_product_pairs.append((numbers_tuple[i], numbers_tuple[j]))

print("Distinct pairs whose product is even:", even_product_pairs)
