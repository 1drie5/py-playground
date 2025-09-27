# Write a program to accept a sequence of comma-separated numbers from the user and generate a tuple with those numbers.

a = [int(i) for i in input("Your List: ").split(',')]
t = tuple(a)
print("RESULTANT TUPLE: ", t)