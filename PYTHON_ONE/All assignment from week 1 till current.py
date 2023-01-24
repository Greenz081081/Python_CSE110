#Compilation of all the assignments from All assignment from week 1 till current
#Author: Emediong Edet
#Purpose: create a Library of reference.
print("Hi there!")
print("My name is Emediong Henry Edet")
print("Let's get to know more about you!")

print()
wellfare = input("So how are you doing today:")
print("Good to know how you are doing!")

first_name = input("What is your first name:")
last_name = input("Please input your last name:")
print("----------------------------------------------")

print()
email = input("Email Address:")
phone = input("Phone Number:")
Job = input("Job title:")
identity = input("ID Number:")
print("----------------------------------------------")

print()
#Getting the IDENTITY card done 
print("Your Identity Card is:")
print(f"Name: {last_name.upper()}, {first_name.capitalize()}")
print(f"Email: {email.capitalize()}")
print(f"Phone: {phone}")
print(f"Job: {Job.capitalize()}")
print(f"ID: {identity}")

#Getting further information for important usage.
print("Please enter the following information:")

hair_colour = input("What is your hair color:")
eyes_colour = input("What is your eye color:")
month_of_training = input("Have you completed any additional training:")

print("If yes, enter the preceeding information:")

training_type = input("Training type:")
year_of_training = input("Year of training completion:")
years_of_experience = input("Years of experience:")
print("----------------------------------------------")

print()
print(f"Hair: {hair_colour:15} Eye: {eyes_colour}")
print("Additional Information:")
print(f"Additional traning completion answer is {month_of_training}")
print(f"Your training type is {training_type}")
print(f"Year of training completion is {year_of_training}")
print(f"Your years of experience is {years_of_experience}")
print("Thank you for the additional information.")


print()
print()
print("Let's keep you entertained as we proceed to the continued part of the info.")
print("Please input the words of your choice!")
print()


adjective_one = input("Adjective:")
animal = input("Animal:")
verb_one = input("Verb:")
exclamation = input("Exclamation:")
verb_two = input("Verb:")
verb_three = input("Verb:")
pronoun = input("Pronoun:")
adjective_two = input("Adjective:")
verb_four = input("Verb:")
verb_five = input("Verb:")
print("-------------------------------------")


print()
print("Lets enjoy your madlib word story!")
print(f"The other day, i was really in touble. It all started when i saw a very {adjective_one}")
print(f"{animal} {verb_one} down the hallway. {exclamation.capitalize()}!. I yelled")
print(f"But all i could think to do was to {verb_two} over and over.")
print(f"Miraculously, that caused it to stop, but not before it tried to {verb_three}")
print(f"right in front of my family. {pronoun.capitalize()} was such an {adjective_two} experience,")
print(f"I {verb_four} over and over again, each time I {verb_five} it.")

print()
print()
print("Great! Hope you enjoyed the little madlib story.")
print("Welcome back, Let's proceed.")
print("-------------------------------------")

print()
print("Hope you gonna enjoy this too!")
print("Lets get to know shapes and areas...")
print("Please input the following informations!")

square_length = float(input("What is the length of a side of a square:"))
rectangle_length = float(input("What is the length of rectangle:"))
rectangle_width = float(input("What is the width of the rectangle:"))
circle_radius_1 = float(input("What is the radius of the circle"))
print("-----------------------------------------------")
print()


import math
area_1 = square_length ** 2
print(f"The area of the square is { area_1}")
area_2 = rectangle_length * rectangle_width
print(f"The area of the rectangle is {area_2}")
area_3 = math.pi * circle_radius_1 ** 2
print(f"The area of the circle is {area_3}")

print()
print()
print("We use a single value to calculate for all the areas of the shapes")
value = float(input("Please input the value to be used:"))
print()
import math 
square_area = value ** 2
circle_radius_2 = math .pi * ( value ** 2 )
cube_volume = value ** 3
sphere_radius = ( 4 / 5) * math.pi * ( value ** 3 )
print("---------------------------------------")
print()
print(f"The area of the sqaure is {square_area}")
print(f"The area of the circle is {circle_radius_2}")
print(f"The area of the cube is {cube_volume}")
print(f"The area of the sphere is {sphere_radius}")
#Calculating the price of meal for both children and adults
print("-------------------------------------")
print()
print("This is to enable us calculate the price, total, and the change of each product purchased! ")
print("Please enter the following informations:")
print()
childs_meal = float(input("What is the price of a child's meal:"))
adults_meal = float(input("What is the price of an adult's meal:"))
childs_appetizer = float(input("What is the price of a chid's appetizer:"))
adults_appetizer = float(input("What is the price of an adult's appetizer:"))
number_of_children = int(input("How many children are there:"))
number_of_adults = int(input("How many adult's are there:"))
sales_tax_rate = float(input("What is the sales tax rate:"))
print("---------------------------------------")
print()
print()
subtotal_1 = (childs_meal + childs_appetizer) * number_of_children
subtotal_2 = (adults_meal + adults_appetizer) * number_of_adults
subtotal = subtotal_1 + subtotal_2
print()
print((f"Subtotal: ${subtotal:.2f}"))
sub_sales_tax = subtotal * sales_tax_rate / ( 100 )
sales_tax = sub_sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
sub_total = subtotal + sales_tax
total = sub_total
print(f"Total: ${total:.2f}")
print()
payment_amount = float(input("What is the payment amount:"))
change = payment_amount - total
print(f"Change: ${change:.2f}")
end = input("---")