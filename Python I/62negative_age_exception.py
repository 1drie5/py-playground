# Write a program to read the age of a person and raise exceptions if age is negative.

def get_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    age = get_age()
    print("The entered age is:", age)
except ValueError as ve:
    print(ve)
