# Write a program to find all the numbers divisible by 5 and 7 between the given range using the lambda function.

def find_numbers_divisible_by_5_and_7(start, end):
    divisible_numbers = list(filter(lambda x: x % 5 == 0 and x % 7 == 0, range(start, end + 1)))
    return divisible_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

divisible_numbers = find_numbers_divisible_by_5_and_7(start_range, end_range)

if divisible_numbers:
    print(f"Numbers divisible by 5 and 7 between {start_range} and {end_range}:")
    print(divisible_numbers)
else:
    print(f"No numbers divisible by 5 and 7 found in the range {start_range} to {end_range}.")
