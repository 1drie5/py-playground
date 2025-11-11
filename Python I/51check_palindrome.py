# Create a module to check if a passed string is a palindrome or not. Write a program to find whether a string is a palindrome or not using this module.

from my_module import *
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(f"{input_str} is a palindrome.")
else:
    print(f"{input_str} is not a palindrome.")
