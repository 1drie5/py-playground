# Write a program to define a function that accepts a string and calculates the number of uppercase letters and lowercase letters.

def count_letters(string):
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count

user_input = input("Enter a string: ")
uppercase, lowercase = count_letters(user_input)
print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
