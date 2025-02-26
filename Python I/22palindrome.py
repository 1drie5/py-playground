# Write a program to read a string and check whether the string is a palindrome or not.

text = input("Enter a string: ")

text = text.replace(" ", "").lower()

length = len(text)
is_palindrome = True
i = 0

while i < length // 2:
    if text[i] != text[length - i - 1]:
        is_palindrome = False
        break
    i += 1

if is_palindrome:
    print(f"""The string "{text}" is a palindrome.""")
else:
    print(f"""The string "{text}" is not a palindrome.""")
