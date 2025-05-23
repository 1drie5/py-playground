# Write a program to concatenate two lists using list comprehension.

a = [int(i) for i in input("1st LIST: ").split()]
b = [int(i) for i in input("2nd LIST: ").split()]
c = []
for i in [a, b]:
    for j in i:
        c.append(j)
print("CONCATENATED LIST: ", c)