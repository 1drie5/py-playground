# Write a program to add two complex numbers by reading the numbers from the user.

complex1 = complex(input("Enter the first complex number (e.g., 3+4j): "))
complex2 = complex(input("Enter the second complex number (e.g., 1-2j): "))
result = complex1 + complex2
print(f"The sum of {complex1} and {complex2} is {result}")
