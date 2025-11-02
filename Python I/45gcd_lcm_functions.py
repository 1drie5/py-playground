# Write a program to find GCD and LCM of two numbers by defining a function to compute GCD and LCM.

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return (a * b) // find_gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)
lcm = find_lcm(num1, num2)

print("GCD:", gcd)
print("LCM:", lcm)
