text = input("Enter a string: ").lower()

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for char in text:
    if char == 'a':
        a_count += 1
    elif char == 'e':
        e_count += 1
    elif char == 'i':
        i_count += 1
    elif char == 'o':
        o_count += 1
    elif char == 'u':
        u_count += 1

print(f"a = {a_count}")
print(f"e = {e_count}")
print(f"i = {i_count}")
print(f"o = {o_count}")
print(f"u = {u_count}")
