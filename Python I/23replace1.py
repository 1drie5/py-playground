# Write a program to get a string from a given string where all occurrences of the last character have been changed to '*', except the last character.

text = input("Enter a string: ")
if text == "":
    print("string empty")
else:
    lastChar = text[-1]
    newtext = ""
    for x in text[:-1]:
        if x == lastChar:
            newtext = newtext + "*"
        else:
            newtext = newtext + x
    newtext = newtext + lastChar
    print(newtext)
