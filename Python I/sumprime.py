# Write a program to find the sum of all prime numbers within a given range.

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

sum_primes = 0

for num in range(start, end + 1):  
    if num < 2:
        continue
    elif num == 2:
        sum_primes += 2
    elif num % 2 == 0:
        continue
    else:
        is_prime = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            sum_primes += num

print("Sum of prime numbers in the range:", sum_primes)
