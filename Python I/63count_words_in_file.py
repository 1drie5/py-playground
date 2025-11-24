# Write a program to accept a file name from the user and count the number of words present in the file.

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            return word_count

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

file_name = input("Enter the file name: ")

word_count = count_words_in_file(file_name)

if word_count is not None:
    print("The number of words in the file is:", word_count)
