# Write a program to calculate the area and perimeter of a rectangle.

length = float(input("Enter the length of the rectangle : "))
breadth = float(input("Enter the breadth of the rectangle : "))
perimeter = 2.0 * (length + breadth)
area = length * breadth
print(f"Perimeter of the rectangle : {perimeter} units")
print(f"Area of the rectangle : {area} square units")