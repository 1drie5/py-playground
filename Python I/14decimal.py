# Write a program to print the decimal equivalents of 1/2, 1/3, 1/4, ..., 1/10 using for loop.

n = int(input("Enter Range: "))
print(f"Decimal equivalents of fractions from 1/2 to 1/{n}:")

for i in range(1,n):
    # print("1/"+str(i+1) + " = " + str(1/(i+1)))
    print(f"1/{i+1} = {1/(i+1):.6f}")
