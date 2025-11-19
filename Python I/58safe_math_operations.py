# Write a program to read two numbers from the user and perform basic mathematical operations (addition, multiplication, subtraction, division) by handling all possible exceptions.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    try:
        print("Division:", num1 / num2)
    except ZeroDivisionError:
        print("Division: Cannot divide by zero")

except ValueError:
    print("Invalid input! Please enter only numbers.")
except Exception as e:
    print("An unexpected error occurred:", e)
