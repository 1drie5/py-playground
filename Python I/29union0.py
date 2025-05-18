# Write a program to find the union of two lists.

list1 = [int(i) for i in input("LIST-1: ").split()]
list2 = [int(i) for i in input("LIST-2: ").split()]
print("Union: ")
for j in range(len(list1)):
    print(list1[j],end=" ")
for i in range(len(list2)):
    c=0
    for j in range(len(list1)):
        if(list2[i]==list1[j]):
            c=1
            break
    if(c==0):
        print(list2[i],end=" ")