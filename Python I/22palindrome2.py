# Write a program to read a string and check whether the string is a palindrome or not.

text = input("Enter a string: ").replace(" ", "").lower()

if text == text[::-1]:
    print(f"""The string "{text}" is a palindrome.""")
else:
    print(f"""The string "{text}" is not a palindrome.""")
