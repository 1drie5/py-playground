# Write a program to swap the value of two variables using a third variable.

a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))

print("Before swapping:")
print(f"a = {a}, b = {b}")

# Swapping logic using third variable
temp = a
a = b
b = temp

print("After swapping:")
print(f"a = {a}, b = {b}")
