def is_palindrome(s):
    return s == s[::-1]

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorial(number):
    if number < 0:
        return None
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
