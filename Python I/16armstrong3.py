# Write a program to check whether a given number is an Armstrong number or not.

num = int(input("Enter a number: "))

num_digits = len(str(num))

sum_of_powers = sum(int(digit) ** num_digits for digit in str(num))

if sum_of_powers == num:
    print(f"Yes, {num} is an Armstrong number.")
else:
    print(f"No, {num} is not an Armstrong number.")
