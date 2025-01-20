# Write a program to compute the GCD of two integer numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

original_a = a
original_b = b

# Division-Based Euclidean Algorithm
while b != 0:
    while b != 0:
        temp = b
        b = a % b
        a = temp
gcd = a

print(f"GCD of {original_a} and {original_b} is {gcd}")
