print("Please Enter the following information")
print()

#Ask for the basic information
first_name = input("First Name:")
last_name = input("Last Name:")

email = input("Email adress:")

phone = input("Phone Number:")


job = input("Job title:")


identity = input("ID number:")

#Ask additional questions
hair_colour = input("Hair colour:")
eye_colour = input(" Eye colour:")
month = input("Starting month:")
Training = input("Conpleted additional training?")

#Now print out the ID card
print("\nThe ID card is:")
print("--------------------------------------")
print(f"{last_name.upper()}, {first_name}")
print(email.lower())
print()
print(phone)
print(job.capitalize())
print(f"ID: {identity}")

print("--------------------------------------")
print()

print("Details collected")
print()

#Get to remember the exact way of which
#you have used to achieve this particular
#stretch requirement.

print(f"Hair: {hair_colour:15}  Eye: {eye_colour}")
print(f"Month: {month:14}  Training: {Training}")

print("--------------------------------------------")
print()
End = input()
