'''
Write a program to calculate simple interest with the following conditions:
-	If the principal amount is less than 2,00,000 the interest rate is 10%.
-	If the principal amount is 2,00,000 - 10,00,000 the interest rate is 12%.
-	If the principal amount is greater than 10,00,000 the interest rate is 15%.
'''
p = float(input(f"Enter principal amount (in Rs.): "))
t = float(input("Enter duration in years (in years): "))

if p < 200000:
    r = 10
elif 200000 <= p <= 1000000:
    r = 12
else:
    r = 15

si = (p * r * t) / 100
amt = p + si

print("\n--- Calculation Results ---")
print(f"Principal Amount: {p}")
print(f"Rate (in %): {r}")
print(f"Time Period: {t} years")
print(f"Interest Amount: Rs. {si:.2f}")
print(f"Total Amount (Principal + Interest): Rs. {amt:.2f}")
