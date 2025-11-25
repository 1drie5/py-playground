# Write a program to reverse the content of a file and store it in another file.

def reverse_file_content(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            reversed_content = content[::-1]

        with open(output_filename, 'w') as output_file:
            output_file.write(reversed_content)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)


input_file_name = input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")

reverse_file_content(input_file_name, output_file_name)
