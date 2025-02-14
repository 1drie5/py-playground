# Write a program that prompts users to enter numbers. This process repeats until the user enters -1. Finally, the program prints the count of prime and composite numbers entered.

prime_count = 0
composite_count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    
    if num == -1:
        break
    
    if num < 2:
        continue

    is_prime = True
    
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_count += 1
    else:
        composite_count += 1

print("Prime numbers entered:", prime_count)
print("Composite numbers entered:", composite_count)
