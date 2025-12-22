import csv

def get_user_input():
    data = []
    n = int(input("Enter number of values: "))
    for _ in range(n):
        value = input("Enter value: ")
        data.append(value)
    return data

def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for value in data:
            writer.writerow([value])

file1 = input("Enter first CSV file name: ")
print("Enter data for first CSV file:")
data1 = get_user_input()
write_to_csv(file1, data1)

file2 = input("\nEnter second CSV file name: ")
print("Enter data for second CSV file:")
data2 = get_user_input()
write_to_csv(file2, data2)

common_values = set(data1).intersection(set(data2))

print("\nCommon values in both CSV files:")
if common_values:
    for value in common_values:
        print(value)
else:
    print("No common values found")
