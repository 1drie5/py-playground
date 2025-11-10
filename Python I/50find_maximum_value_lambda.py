# Write a program to find the maximum value from a list using the lambda function.

# Program: Find the maximum value from a list using a lambda function

def find_maximum_value(input_list):
    if not input_list:
        return None
    return max(input_list, key=lambda x: x)

input_str = input("Enter a list of numbers separated by commas: ").strip()

if not input_str:
    print("No input provided.")
else:
    try:
        input_list = [int(x) for x in input_str.split(',') if x.strip()]
        if not input_list:
            print("No valid numbers entered.")
        else:
            max_value = find_maximum_value(input_list)
            print(f"The maximum value in the list is: {max_value}")
    except ValueError:
        print("Invalid input. Please enter only integers separated by commas.")
