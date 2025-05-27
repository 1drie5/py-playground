# Write a program to find the distinct pair of numbers whose product is odd from a list of integers.

a = [int(i) for i in input("LIST: ").split()]
out = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if(a[i] * a[j]) % 2 == 1:
            b = [min(a[i], a[j]), max(a[i], a[j])]
            if b in out:
                continue
            else:
                out.append(b)
print("RESULT: ", out)