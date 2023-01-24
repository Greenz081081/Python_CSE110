# week 04 assignment
# Purpose: Write a program to convert from fahrenhiet to celsius.
# Display the result to one decimal place of precision.
# Author: Emediong Edet
print()
print()

temperature_fahrenhiet = float(input("What is the temperature in Fahrenhiet?"))
sub_temperature_celsius_1 = temperature_fahrenhiet - 32 
sub_temperature_celsius_2 = sub_temperature_celsius_1 * 5 / 9

print(f"The temperature in celsius is {sub_temperature_celsius_2 :.1f} degrees.")
print(f"The temperature in celsius is {sub_temperature_celsius_2 :.1e} degrees.")
