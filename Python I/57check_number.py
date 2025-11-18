# Write a program to read a number from the user. If the number is positive or zero, print it, otherwise raise an exception.

try:
    num = float(input("Enter a number: "))
    if num >= 0:
        print("The number is: ", num)
    else:
        raise ValueError("The number is negative.")
except ValueError as e:
    print("Error: ", e)
