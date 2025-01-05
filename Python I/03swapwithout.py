# Write a program to swap the value of two variables without using a third variable.

a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))
print("Before swapping:")
print(f"a = {a}, b = {b}")

# Swapping logic without using third variable
a = a + b
b = a - b
a = a - b

print("After swapping:")
print(f"a = {a}, b = {b}")