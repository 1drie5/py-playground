# Write a program to add two complex numbers by reading the numbers from the user.

# Read the first complex number
real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
complex1 = complex(real1, imag1)

# Read the second complex number
real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))
complex2 = complex(real2, imag2)

# Add the complex numbers
result = complex1 + complex2

# Display the result
print(f"The sum of {complex1} and {complex2} is {result}")
