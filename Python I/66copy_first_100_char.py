# Write a program to copy the first 100 characters of a binary file into another.

def copy_first_100_chars(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as input_file:
            with open(output_filename, 'wb') as output_file:
                first_100_chars = input_file.read(100)
                output_file.write(first_100_chars)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)


input_file_name = input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")

copy_first_100_chars(input_file_name, output_file_name)
