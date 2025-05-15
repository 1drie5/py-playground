# Write a program to find the maximum and minimum of a list of numbers without using built-in functions.

try:
    numbers = [int(i) for i in input("Enter numbers separated by spaces: ").split()]
except ValueError:
    print("Please enter only integers.")
    exit()

if len(numbers) == 0:
    print("The list is empty.")

else:    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    print("Maximum value:", maximum)
    print("Minimum value:", minimum)