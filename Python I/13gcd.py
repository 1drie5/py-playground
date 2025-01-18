# Write a program to compute the GCD of two integer numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

hcf = 0
for i in range(1,min(a,b),1):
    if(a%i==0 and b%i==0):
        hcf=i

print(f"GCD of {a} and {b} is {hcf}")

