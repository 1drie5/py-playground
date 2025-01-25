# Program to check whether a given number is an Armstrong number or not.

num = int(input("Enter number: "))
copy1 = num
copy2 = num
count = 0
arm = 0
digit = 0

while copy1 != 0:
    count += 1
    copy1 //= 10

while copy2 != 0:
    digit = copy2 % 10
    arm += digit ** count  
    copy2 //= 10

if arm == num:
    print(f"Yes, {num} is an Armstrong number.")
else:
    print(f"No, {num} is not an Armstrong number.")
