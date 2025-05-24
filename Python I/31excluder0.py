# Write a program to create a list from two given lists ‘list1’ and ‘list2’ of numbers such that it contains numbers that are present in ‘list2’ but not in ‘list1’.

list1 = [int(i) for i in input("Enter elements of list1: ").split()]
list2 = [int(i) for i in input("Enter elements of list2: ").split()]

result = []

for i in range(len(list2)):
    found = False
    for j in range(len(list1)):
        if list2[i] == list1[j]:
            found = True
            break
    if not found:
        result.append(list2[i])

print("Numbers present in list2 but not in list1:", result)