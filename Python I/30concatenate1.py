# Write a program to concatenate two lists using list comprehension.

list1 = [int(i) for i in input("Enter elements of List 1 (space-separated): ").split()]
list2 = [int(i) for i in input("Enter elements of List 2 (space-separated): ").split()]

c = [j for i in [list1, list2] for j in i]

print("CONCATENATED LIST:", c)