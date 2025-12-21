import csv

subjects = []
marks = []

filename = input("Enter csv file name: ")

with open(filename, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        subjects.append(row['Subject'])
        marks.append(int(row['Marks']))

data_dict = {}
for i in range(len(subjects)):
    data_dict[subjects[i]] = marks[i]

print(data_dict)
