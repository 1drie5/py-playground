# Write a program to get the LCM of two positive integers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a == 0 or b == 0:
    print("LCM is not defined for zero.")
else:
    original_a = a
    original_b = b

    while b != 0:
        temp = b
        b = a % b
        a = temp

    gcd = a

    lcm = (original_a * original_b) // gcd

    print(f"LCM of {original_a} and {original_b} is {lcm}")
