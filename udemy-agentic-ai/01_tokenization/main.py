import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey There! I am iddu..." 
token = enc.encode(text) #  [25216, 3274, 0, 357, 939, 1211, 698, 1008]

print("Tokens: ", token)

decoded = enc.decode([25216, 3274, 0, 357, 939, 1211, 698, 1008])
print("Decoded: ", decoded) # Hey There! I am iddu

decoded69 = enc.decode([69, 6969, 69696])
print("Decoded69: ", decoded69)

