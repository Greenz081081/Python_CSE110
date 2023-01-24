print("Please enter the following information!")
print()

#Ask some basic questions to start with, also remember all the rules needed to run a decent programme

first_name = input("Enter your first name:")
last_name = input("Enter your last name:")

email = input("Email address:")
phone = input("Phone number:")
Job = input("Job title:")
identity =input("ID number:")
 
print("---------------------------------")

#Ask other additional questions as a requirement for the strecth prove

hair_colour = input("Hair colour:")
eyes_colour = input("Eye colour:")
month = input("Starting month:")
Training = input("Completed any additional training?")

#Now print the ID card
print("\nThe ID card is")
print(f"{last_name.upper()}, {first_name}")
print(email.lower())
print(phone)
print(Job)
print(f"ID:{identity}")

print("------------------------------------")
print()
print(f"Hair: {hair_colour:15} Eye:{eyes_colour}")
print(f"Month: {month:14} Training: {Training}")
print("------------------------------------")
print()
End = input("__")