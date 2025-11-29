# Write a program to copy one Python script into another in such a way that all comment lines are skipped and not copied to the destination file.

def copy_without_comments(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            with open(output_filename, 'w') as output_file:
                for line in input_file:
                    if not line.strip().startswith('#'):
                        output_file.write(line)
                        
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

input_file_name = input("Enter the input file name: ")
output_file_name = input("Enter the output file name: ")
copy_without_comments(input_file_name, output_file_name)
