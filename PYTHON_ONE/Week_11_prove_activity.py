# Task: Write a program to analyze a dataset containing information
# about life expectances over the years throughout the countries of the world.

# What is the year and country that has the lowest life expectancy in the dataset?

# What is the year and country that has the highest life expectancy in the dataset?

# Allow the user to type in a year, then, find the average life expectancy for that year.
# Then find the country with the minimum and the one with the maximum life expectancies 
# for that year.


# Load the dataset in your Python program
skip = 0
lowest = 1000
lowest_year = 1000
lowest_country = None
highest = 0
highest_year = 0
highest_country = None


user_lowest = 99999
user_lowest_year = 99999
user_lowest_country = None

user_highest = 0
user_highest_year = 0
user_highest_country = None

country_lowest = 99999
user_country_lowest_year = 99999
user_country_lowest_country = None

country_highest = 0
user_country_highest_year = 0
user_country_highest_country = None

choice_year = []
choice_country = []
# sum = 0
# average = 0


# Allow the user to type in a year
user_input = int(input("Enter the year of interest:"))
# Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
user_country_input = input("Enter the country of interest:")
with open("life-expectancy.csv") as life_expectancy_files:

       
# Iterate through the data line by line
        for data in life_expectancy_files:
                skip = skip + 1
                data = data.strip()
# Split each line into parts        
                parts = data.split(",")

                if skip > 1:
                        country =  parts[0]
                        code = parts[1]
                        year = int(parts[2])
                        life_expectancy = float(parts[3])
                        
                        # print(f"{country} - {code} - {year} - {life_expectancy}")

                       

# What is the year and country that has the lowest life expectancy in the dataset?
                        if lowest > (life_expectancy):
                                lowest = (life_expectancy)
                                lowest_year = year
                                lowest_country = country

# What is the year and country that has the highest life expectancy in the dataset?
                        if highest < life_expectancy:
                                highest = life_expectancy
                                highest_year = year
                                highest_country = country


                        #  find the country with the maximum life expectancies for that year.
                        if year == user_input and user_highest < life_expectancy:   
                                choice_year.append(user_input)                   
                                user_highest = life_expectancy            
                                user_highest_country = country

                        sum = 0
                        average = 0
                        for x in choice_year:
                                sum += x
                                average += 1
                                average = sum / average
                                        # length_1 = len(choice_year)
                                        # average = average + life_expectancy

                        #  find the country with the minimum life expectancies for that year                    
                        if year == user_input and user_lowest > life_expectancy:
                                choice_year.append(user_input)              
                                user_lowest = life_expectancy                
                                user_lowest_country = country
                               
                      
                        
                        if country.lower() == user_country_input.lower() and country_lowest > life_expectancy:
                                choice_country.append(user_country_input)
                                user_country_lowest_country = country
                                country_lowest = life_expectancy

                                length_2 = len(choice_year)                            
                                average = average + life_expectancy

                        if country.lower() == user_country_input.lower() and country_highest < life_expectancy:
                                choice_country.append(user_country_input)
                                user_country_highest_country = country
                                country_highest = life_expectancy
                             


# first_average = (average / length_1)
# second_average = (average / length_2)
                            


print()
print()
print(f"The overall max life expectancy is: {highest} from {highest_country} in {highest_year}")
print(f"The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}")
print()
print()
print()
print(f"For the year {user_input}:")
print(f"The Average life expectancy across all country was:{average:.2f}")
print(f"The max life expectancy was in {user_highest_country} with {user_highest}")
print(f"The min life expectancy was in {user_lowest_country} with {user_lowest}")
print()
print()
print(f"For the country {user_country_input.capitalize()}:")
# print(f"The Average life expectancy for this country was: {average_2:.2f}")
print(f"The max life expectancy was {country_highest} ")
print(f"The min life expectancy was {country_lowest} ")

     




ages = [18,19,20,19,19,21,23,24]
sum = 0
number_of_data_points = 0
for x in ages:
        sum += x
        print(x)
        number_of_data_points += 1
        print(sum)
        print(number_of_data_points)
        print("average = ", sum / number_of_data_points)





                


                      




                      







 