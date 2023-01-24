#CCSE 110
print("Title: Assignment Continuation")
print("Author: Emediong Edet")
print("Purpose: Print data on screen")
print("-----------------------------")
print()

#This is a programme code written for the 
#purpose of creating a personal 
#ID information for a recipient.
print("Please enter the following information!")
print()
print("-----------------------------")
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")

email = input("Email address:")
phone = input("Phone number:")
job = input("Job title:")
identity = input("ID number:")
nationality = input("Country:")
state = input("State of province:")
city = input("City:")
print("-----------------------------")

#Further requirements for more information
hair = input("Hair colour:")
eye = input("Eye colour:")
month = input("Starting month:")
training = input("Completed any additional training?")
print()
print("-----------------------------")

#ID card sample print out:
print("\nPersonal Information ID")
print()
print("----------------------------")
print(f"{last_name.upper()}, {first_name}")
print(email.capitalize())
print(phone)
print(job)
print()
print("----------------------------")
print(f"ID:{identity}")
print(nationality)
print(state)
print(city)
print()
print("----------------------------")
print(f"Hair:{hair:18} Eye:{eye}")
print(f"Month:{month:17} Training:{training}")
print()
print("----------------------------")
end = input(".")
