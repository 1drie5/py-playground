# Write a program to count the occurrences of a word in a given sentence.

sentence = input("Enter a sentence: ").strip().lower()
if not sentence:
    print("Empty string")
else:
    word = input("Enter the word to count: ").strip().lower()
    if not word:
        print("No word given")
    else:
        word_count = sentence.split().count(word)
        print(f"The word '{word}' appears {word_count} time(s) in the sentence.")
