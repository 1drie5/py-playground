# Write a program to rotate the value of x, y, and z such that x has the value of y, y has the value of z and z has the value of x.

x = int(input("Enter X number "))
y = int(input("Enter Y number "))
z = int(input("Enter Z number "))

print("\nBefore rotation:")
print(f"x = {x}, y = {y}, z = {z}")

# Rotate the values
x, y, z = y, z, x

print("\nAfter rotation:")
print(f"x = {x}, y = {y}, z = {z}")
