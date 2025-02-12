# Write a program to find the sum of all prime numbers within a given range.

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if end < 2:
    print("Sum of prime numbers in the range: 0")
else:
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(end**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, end + 1, num):
                sieve[multiple] = False

    sum_primes = sum(i for i in range(start, end + 1) if sieve[i])

    print("Sum of prime numbers in the range:", sum_primes)
