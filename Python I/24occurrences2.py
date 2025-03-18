# Write a program to count the occurrences of a word in a given sentence.

text=input("Enter a string: ")
if not text:
    print("Empty string")
else:
    wrd=input("Enter the word to count: ")
    if not wrd:
        print("No word given")
    else:
        str=[i for i in text.split()]
        occ=0
        for i in str:
            if i.lower()==wrd.lower():
                occ+=1
        print(f"The word '{wrd}' appears {occ} time(s) in the sentence.")