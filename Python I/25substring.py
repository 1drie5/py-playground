# Write a program to get all substrings of a given string.

text = input("Enter a string: ")

if len(text) == 0:
    print("string empty")
else:
    length = len(text)
    for i in range (length):
        for j in range (i,length):
            print(text[i:j+1])