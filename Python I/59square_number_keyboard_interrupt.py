# Write a program to read a number from the user and print its square. Generate KeyboardIntrrupt exception if Ctrl + C is pressed instead of a number.

try:
    num = float(input("Enter a number: "))
    print("Square of the number is:", num * num)

except KeyboardInterrupt:
    print("\nKeyboardInterrupt occurred! You pressed Ctrl + C.")

except ValueError:
    print("Invalid input! Please enter a valid number.")
