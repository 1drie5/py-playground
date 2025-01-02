# Write a program to convert temperature from degree Celsius to degree Fahrenheit.


temperature_in_celcius = float(input("Enter temperature in Celsius "))
print(f"Temperature in Celsius = {temperature_in_celcius}")

temperature_in_fahrenheit = temperature_in_celcius * (9/5) + 32
print(f"Temperaturn in Fahrenheit = {temperature_in_fahrenheit}")
