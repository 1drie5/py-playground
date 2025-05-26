# Write a program to create a list from two given lists ‘list1’ and ‘list2’ of numbers such that it contains numbers that are present in ‘list2’ but not in ‘list1’.

a = [int(i) for i in input("Enter elements of list1: ").split()]
b = [int(i) for i in input("Enter elements of list2: ").split()]
c = []
for i in b:
    if i not in a:
        c.append(i)
print("Numbers present in list2 but not in list1:", c)
