def split_words(file_name):
    try:
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                print("Line: ", line_number)
                words = line.split()
                for word in words:
                    print(word)
                print()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    file_name = input("Enter the name of the text file: ")
    split_words(file_name)

if __name__ == "__main__":
    main()
