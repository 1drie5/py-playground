# Write a program to sort (ascending order) a dictionary by value.

data = {}
n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value
    
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Original Dictionary:", data)
print("Dictionary Sorted by Value (Ascending):", sorted_data)
