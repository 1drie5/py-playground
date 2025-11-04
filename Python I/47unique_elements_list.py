# Write a program to find all the unique elements of a list by defining a function.

def find_unique_elements(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

user_input = input("Enter a list of elements (separated by spaces): ")
user_list = user_input.split()

unique_list = find_unique_elements(user_list)
print("Unique elements:", unique_list)
