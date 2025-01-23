# Write a program to check whether a given number is a prime number or not.

num = int(input("Enter Number: "))

if num < 2:
    print("No, it is not a Prime Number")  # Numbers less than 2 are not prime
else:
    c = 0
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to sqrt(num)
        if num % i == 0:
            c += 1
            break

    if c == 0:
        print("Yes, it is a Prime Number")
    else:
        print("No, it is not a Prime Number")
