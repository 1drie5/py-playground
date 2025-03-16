# Write a program to count the occurrences of a word in a given sentence.

sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Empty string!")
else:
    sentence+=" "
    word = input("Enter the word to count: ").strip()
    if not word:
        print("No word given!")
    else:
        current_word = ""
        word_count = 0  
        i = 0

        while i < len(sentence):
            char = sentence[i]

            if char != " ":  
                current_word += char
            else:
                if current_word.lower() == word.lower():
                    word_count += 1
                current_word = ""
    
            i += 1

        print(f"The word '{word}' appears {word_count} time(s) in the sentence.")





