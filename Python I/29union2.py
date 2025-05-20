# Write a program to find the union of two lists.

a = [int(i) for i in input("LIST-1: ").split()]
b = [int(i) for i in input("LIST-2: ").split()]
a.extend(b)
a = list(set(a))
a.sort()
print("Union: ", *a)