from csv import DictWriter

data = []

num_entries = int(input("Enter the number of entries: "))

for _ in range(num_entries):
    roll = int(input("Enter Roll Number: "))
    subject = input("Enter Subject: ")
    marks = int(input("Enter Marks: "))
    data.append({'Roll': roll, 'Subject': subject, 'Marks': marks})

filename = input("Enter output csv file name: ")

with open(filename, 'w', newline='') as csvf:
    fields = list(data[0].keys())
    obj = DictWriter(csvf, fieldnames=fields)
    obj.writeheader()
    obj.writerows(data)

print("Data has been written to file")
