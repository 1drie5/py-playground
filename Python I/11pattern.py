'''
Write a program to print the following patterns:
(a)  1
     2, 3
     4, 5, 6
     7, 8, 9, 10
     11, 12, 13, 14, 15

(b) * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            *
'''
n = int(input("\nEnter number of lines for pattern (a): "))
i=0; j=0; c=1
for i in range(n):
    for j in range(i+1):
        if(i==j):
            print(c)
        else:
            print(c , end=', ')
        c+=1

n = int(input("\nEnter number of lines for pattern (b): "))
for i in range(n):
    print("  " * i, end="")
    print("* " * (2 * (n - i) - 1))
