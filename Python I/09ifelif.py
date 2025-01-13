# Write a program to sort three numbers using if-elif-else.

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

print(f"Unsorted order: {a}, {b}, {c}")

# Sorting logic using if-elif-else
if a <= b and a <= c:
    if b <= c:
        print(f"Sorted order: {a} < {b} < {c}")
    else:
        print(f"Sorted order: {a} < {c} < {b}")
elif b <= a and b <= c:
    if a <= c:
        print(f"Sorted order: {b} < {a} < {c}")
    else:
        print(f"Sorted order: {b} < {c} < {a}")
else:  # c is the smallest
    if a <= b:
        print(f"Sorted order: {c} < {a} < {b}")
    else:
        print(f"Sorted order: {c} < {b} < {a}")
