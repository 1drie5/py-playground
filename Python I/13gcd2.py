# Write a program to compute the GCD of two integer numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

original_a = a
original_b = b 

# Subtractive Euclidean Algorithm
while a != 0 and b != 0:
    if a == b:
        gcd = a
        break
    elif a > b:
        a -= b
    else:
        b -= a

if a != 0:
    gcd = a
else:
    gcd = b

print(f"GCD of {original_a} and {original_b} is {gcd}")
