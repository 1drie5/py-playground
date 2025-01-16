# Write a program using a while loop to print all the odd numbers within a given range.

start=int(input("Enter starting range: "))
end=int(input("Enter ending range: "))
while (start<=end):
    if(start%2==1):
        print(start , end = ' ')
    start += 1
