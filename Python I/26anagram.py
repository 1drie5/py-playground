# Write a program to detect whether two strings are anagrams or not.

str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()

if len(str1) == 0 or len(str2) == 0:
    print("One or both strings are empty.")
elif len(str1) != len(str2):
    print("The strings are not anagrams.")
elif sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")