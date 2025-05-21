# Write a program to concatenate two lists using list comprehension.

list1 = [int(i) for i in input("Enter elements of List 1 (space-separated): ").split()]
list2 = [int(i) for i in input("Enter elements of List 2 (space-separated): ").split()]

concatenated = [item for item in list1] + [item for item in list2]

print("Concatenated List:", concatenated)
