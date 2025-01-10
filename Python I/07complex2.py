# Write a program to add two complex numbers by reading the numbers from the user.

print("Enter four integers (a b c d), where a and b are the real and imaginary parts of the first complex number, and c and d are for the second:")
a, b, c, d = map(int, input().split())
print("The sum of the two complex numbers is:", complex(a, b) + complex(c, d))
