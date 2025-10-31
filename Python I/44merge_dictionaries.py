# Write a program to merge two dictionaries.

dict1 = {}
dict2 = {}

n1 = int(input("Enter the number of elements in the first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

n2 = int(input("\nEnter the number of elements in the second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

print("\nFirst Dictionary:", dict1)
print("Second Dictionary:", dict2)

# Merging dictionaries
merged_dict = dict1.copy()
merged_dict.update(dict2)

print("\nMerged Dictionary:", merged_dict)
