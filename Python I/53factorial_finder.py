# Create a module to find the factorial of a number and import the module from the main program to find the factorial of a given number.

from my_module import factorial

num = int(input("Enter a number to find its factorial: "))

fact = factorial(num)

if fact is not None:
    print(f"The factorial of {num} is: {fact}")
else:
    print("Factorial is not defined for negative numbers.")
