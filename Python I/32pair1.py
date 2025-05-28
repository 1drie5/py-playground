# Write a program to find the distinct pair of numbers whose product is odd from a list of integers.

numbers = [int(i) for i in input("Enter integers separated by spaces: ").split()]

print("Distinct pairs with odd product:")

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] % 2 != 0 and numbers[j] % 2 != 0:
            print(f"({numbers[i]}, {numbers[j]})")
            found = True

if not found:
    print("No such pair found.")