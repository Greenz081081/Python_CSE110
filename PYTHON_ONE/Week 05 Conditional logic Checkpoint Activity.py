#File: Week 05 Programming activity
#Purpose: Practice the mechanics of IF statements.
#Author: Emediong Edet
#Activity: Checkpoint Activity
# print()
# print("----------------------------------------")
# print("----------------------------------------")
# first_number = int(input('What is the first number:'))
# second_number = int(input('What is the second number:'))
# if first_number > second_number:
#     print("The first number is greater")
    
# else:
#     print("The first number is not greater")
   
# if first_number == second_number:
#     print("The numbers are equal")
    
# else:
#     print("The numbers are not equal")
   
# if second_number > first_number:
#     print("The second number is greater")
   
# else:
#     print("The second number is not greater")
#     print()
#     print()
# animal = input("What is your favorite animal:")
# if animal.lower() == "cheetah":
#     print("That's my favorite animal too.")

# else:
#     print("That one is not my favorite animal")
#     print("--------------------------------------")
#     print("--------------------------------------")
#     print()

#File: Team Activity week 05
#Purpose: Write a program that determines the letter grade for a course.
#Author: Emediong Edet

print("Please input information")
grade_percentage = int(input("What is your grade percentage:"))

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >=60:
    letter = "D"
else:
    letter  = "F" 

print(f"Your grade percentage is {letter}")

#if grade_percentage >= 70:
#    comment = "Congratulations"
#else:
#    comment = "Good, but try harder next time."
#print(comment)
print()
sign = ""
last_digit = grade_percentage % 10
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
if grade_percentage >= 93:
    sign = ""
if letter == "F":
    sign = ""
print(f"Your letter grade is {letter}{sign}")

if grade_percentage >= 70:
    print("Congratulations! You have passed.")
else:
    print("Good! But try harder next time.")


