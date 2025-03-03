# Write a program to get a string from a given string where all occurrences of the last character have been changed to '*', except the last character.

text = input("Enter a string: ")
if text == "":
    print("string empty")
else:
    print(text[:-1].replace(text[-1], "*") + text[-1])
