'''
Write a program to accept the principal amount, rate of interest, and duration from the user. 
Calculate the interest amount and the total amount (principal + interest).
'''

p = float(input(f"Enter principal amount (in Rs.): "))
r = float(input("Enter rate (in %): "))
t = float(input("Enter duration in years (in years): "))

si =  (p*r*t)/100.0
amt = p + si

print("\n--- Calculation Results ---")
print(f"Interest Amount: Rs. {si:.2f}")
print(f"Total Amount (Principal + Interest): Rs. {amt:.2f}")
