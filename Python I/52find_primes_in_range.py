# Create a module to check whether a number is a prime or not. Write a program to find the prime numbers between two limits using this module.

from my_module import is_prime

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

prime_numbers = [num for num in range(lower_limit, upper_limit + 1) if is_prime(num)]
print(f"Prime numbers between {lower_limit} and {upper_limit}: {prime_numbers}")
