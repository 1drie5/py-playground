# Write a program to print the even numbers from a given list using the lambda function.

def find_even_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

user_input = input("Enter a list of numbers (separated by spaces): ")
number_list = list(map(int, user_input.split()))
even_list = find_even_numbers(number_list)
print("Even numbers from the given list:", even_list)
