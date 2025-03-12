# Write a program to get a string from a given string where all occurrences of the last character have been changed to '*', except the last character.

text = input("Enter a string: ")

if not text:
    print("string empty")
else:
    lastChar = text[-1]
    newtext = "".join("*" if x == lastChar else x for x in text[:-1]) + lastChar
    print(newtext)
