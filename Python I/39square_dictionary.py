# Write a program to create a dictionary that contains (i, i*i) such that i is an integral number between 1 and n (both included).

number_limit = int(input("Enter the limit: "))

square_dict = {}
for i in range(1, number_limit + 1):
    square_dict[i] = i * i

print("Resultant Dictionary:", square_dict)