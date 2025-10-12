# Write a program to insert a new element into a tuple by taking user input such that the inserted element is the addition of all elements in the tuple, without using built-in functions.

numbers = ()

n = int(input("Enter the size of the tuple: "))

print("Enter the elements:")
for i in range(n):
    value = int(input())
    numbers = numbers + (value,)

print("\nInitial Tuple:", numbers)

total = 0
for num in numbers:
    total = total + num

numbers = numbers + (total,)

print("\nResultant Tuple:", numbers)