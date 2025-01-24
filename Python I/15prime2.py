# Write a program to check whether a given number is a prime number or not.

num = int(input("Enter Number: "))

if num < 2:
    print("No, it is not a Prime Number")
elif num == 2:
    print("Yes, it is a Prime Number")
elif num % 2 == 0:
    print("No, it is not a Prime Number")
else:
    # Check divisors from 3 to sqrt(num), skipping even numbers
    is_prime = True
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Yes, it is a Prime Number")
    else:
        print("No, it is not a Prime Number")
