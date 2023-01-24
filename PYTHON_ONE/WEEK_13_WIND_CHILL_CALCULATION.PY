# Your assignment is to write a program that asks the user for a temperature and
# then shows the wind chill values for various wind speeds at that temperature.

# Your program should compute and display the wind chill for wind speeds
# of 5, 10, 15, ..., 60 miles per hour, just like the National Weather Service
# chart does. To help users who are more familiar with Celsius, your
# program should allow temperature to be entered in either Celsius or
# Fahrenheit, and if needed, convert the Celsius temperature to Fahrenheit
# before using the formula.

# Write a function to calculate and return the wind chill based on a given temperature and wind speed.

# Write a function to convert from Celsius to Fahrenheit.
# The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.

# Allow the user to enter the temperature in Celsius of Fahrenheit.  
# If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.

# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, 
# and calculate and display the wind chill for each of these wind speeds.

# Display the wind chill value to 2 decimals of precision.

# FORMULA = Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
        #   Where,T= Air Temperature (ºF) V= Wind Speed (mph)


     
def calculate_wind_chill():
    windChill = 35.74 + 0.6215 * celsius_temperature - 35.75 * ( wind ** 0.16) + 0.4275 * celsius_temperature * (wind **0.16) 
    return windChill

celsius_temperature = float(input("What is the Temperature?"))
Decision = input("Fahrenheit or Celsius (F/C)?") 
convert_celsius = celsius_temperature *  (9 / 5)  +  32

F = celsius_temperature
C = convert_celsius

def convert_to_fahrenheit(convert_celsius):    
        convert_celsius = celsius_temperature *  (9 / 5)  +  32
wind = 0        
for wind in range(5,65,5):
    convert_to_fahrenheit(celsius_temperature)
    if Decision.lower() == "F":
        print(f"At temperature {celsius_temperature}F, and wind speed {wind}mph, the windchill is: {calculate_wind_chill():.2f}")

    else:
        Decision.lower() == "C"
        print(f"At temperature {celsius_temperature}F, and wind speed {wind}mph, the windchill is: {calculate_wind_chill():.2f}")
# print(convert_celsius)










    






# convert_celsius = temperature_celsius * (9/5) + 32

           
# windChill = 35.74 + (0.6215 * temp) - (35.75 * wind ** 0.16) + (0.4275 * temp * wind **0.16)          

# print(f"At temperature {temperature_celsius}, and wind speed {wind_speeds}, the windchill is:{windChill}")
            



    # return 35.74 + (0.6215 * temp) - (35.75 * wind ** 0.16) + (0.4275 * temp * wind **0.16)


