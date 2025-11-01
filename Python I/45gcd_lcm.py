# Write a program to find GCD and LCM of two numbers without using built-in functions.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Find GCD
if a > b:
    smaller = b
else:
    smaller = a

for i in range(1, smaller + 1):
    if (a % i == 0) and (b % i == 0):
        gcd = i

# Find LCM
lcm = (a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)
