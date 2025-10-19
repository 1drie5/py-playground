# Write a program to count the numbers of characters in a string and store them in a dictionary.

input_string = input("Enter a string: ")

char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character Count:", char_count)
