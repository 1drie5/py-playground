'''
Write a program to calculate simple interest with the following conditions:
-	If the principal amount is less than 2,00,000 the interest rate is 10%.
-	If the principal amount is 2,00,000 - 10,00,000 the interest rate is 12%.
-	If the principal amount is greater than 10,00,000 the interest rate is 15%.
'''
p = int(input(f"Enter principal amount (in Rs.): "))
t = int(input("Enter duration in years (in years): "))

if p < 200000:
    si = (p * 10 * t) / 100
elif 200000 <= p <= 1000000:
    si = (p * 12 * t) / 100
else:
    si = (p * 15 * t) / 100

amt = p + si

print("\n--- Calculation Results ---")
print(f"Principal Amount: {p}")
print(f"Time Period: {t} years")
print(f"Interest Amount: Rs. {si:.2f}")
print(f"Total Amount (Principal + Interest): Rs. {amt:.2f}")
