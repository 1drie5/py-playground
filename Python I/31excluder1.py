# Write a program to create a list from two given lists ‘list1’ and ‘list2’ of numbers such that it contains numbers that are present in ‘list2’ but not in ‘list1’.

list1 = [int(i) for i in input("Enter elements of list1: ").split()]
list2 = [int(i) for i in input("Enter elements of list2: ").split()]

result = [x for x in list2 if x not in list1]

print("Numbers present in list2 but not in list1:", result)