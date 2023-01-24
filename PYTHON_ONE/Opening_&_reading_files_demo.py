# opening and reading files from python
# with open("courses.txt") as courses_file:

#     for courses in courses_file:
#         print(courses)

# print("The file is closed now")




# # splitting strinngs in python
# sentence = "Programming building blocks"

# sentence_parts = sentence.split()
# print(sentence)
# print()
# print(sentence_parts)

# third = sentence_parts[1]
# print()
# print(third)




# # Removing whitespace from strings 
# name = "      Brother, Emediong       \n"

# name = name.strip()


# print(f"-----{name}----")
# print(f"-----{space}-----")


#Putting it together: Reading files and parsing strings
with open("courses.txt") as courses_file:
    for course in courses_file:
        course = course.strip()

        parts = course.split(",")

        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3


        print(f"{name} - Grade: {grade} - After Bonus: {bonus_grade}")
      
      

