# Write a program to find the union of two lists.

list1 = [int(i) for i in input("LIST-1: ").split()]
list2 = [int(i) for i in input("LIST-2: ").split()]

union = []

for x in list1:
    if x not in union:
        union.append(x)

for x in list2:
    if x not in union:
        union.append(x)

print("Union:", *union)