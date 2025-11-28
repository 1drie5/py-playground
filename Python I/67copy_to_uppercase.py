# Write a program to copy the content of the text file to another file by converting all lowercase characters to uppercase.

def copy_convert_to_uppercase(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            with open(output_filename, 'w') as output_file:
                for line in input_file:
                    converted_line = line.upper()
                    output_file.write(converted_line)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

input_file_name = input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")
copy_convert_to_uppercase(input_file_name, output_file_name)
