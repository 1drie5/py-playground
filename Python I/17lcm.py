# Write a program to get the LCM of two positive integers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == 0 or b == 0:
    print("LCM is not defined for zero.")
else:
    max_num = max(a, b)

    while True:
        if max_num % a == 0 and max_num % b == 0:
            print("LCM of", a, "and", b, "is", max_num)
            break
        max_num += 1
