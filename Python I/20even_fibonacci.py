# Write a program to find the sum of the even-valued terms of the Fibonacci series up to 100.

# Multiple Assignment
a, b = 0, 1
sum_even = 0

while a <= 100:
    if a % 2 == 0:
        sum_even += a
    
    # temp = a
    # a = b
    # b = temp + b

    # Multiple Assignment	
    a, b = b, a + b

print("Sum of even Fibonacci terms up to 100:", sum_even)
