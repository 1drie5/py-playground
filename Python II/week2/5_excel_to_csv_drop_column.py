import pandas as pd

excel_file = input("Enter Excel file name: ")
csv_file = input("Enter output CSV file name: ")

try:
    data = pd.read_excel(excel_file)
    data = data.iloc[:, :-1]
    data.to_csv(csv_file, index=False)
    print("CSV file created successfully without the last column.")

except FileNotFoundError:
    print("Error: Excel file not found.")

except Exception as e:
    print("An error occurred:", e)
