# Write a program to print each line of a file in reverse order.

def print_lines_in_reverse(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                print(line.rstrip()[::-1])
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

file_name = input("Enter the file name: ")
print_lines_in_reverse(file_name)
