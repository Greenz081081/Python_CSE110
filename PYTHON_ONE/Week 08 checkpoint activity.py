#Week 08 checkpoint activity
#Purpose: Demonstrate your understanding for loops

# colors = ["red", "blue", "green", "yellow"]
# for item in colors:
#       print(item)

# print()

# numbers = range(9) 
# for i in range(1,9):
#       print(i)

# print()

# even_numbers = range(2,22)
# for i in range(2,22,2):
#       print(i)

    
#In previous lessons you've used formatting strings to display numbers with a certain number of decimal 
#places "{the_number:.2f}". In a similar way, you can specify the number of spaces to take up by 
#including that number after the colon as follows:


# print()
# the_number = 128
# print(f"{the_number}")
# print(f"{the_number:1}")
# print(f"{the_number:2}")
# print(f"{the_number:3}")
# print(f"{the_number:5}")
# print(f"{the_number:10}")

# Notice that if the number you specify is less than or equal to the number of digits in the number,
# it will simply display the number normally.


#Task: create a program that generates a multiplication table
#Purpose: Use python to solve problems



# print()
# user_choice = int(input("How many columns and rows do you want in your multipication table?") )

# range_size = user_choice + 1

# for row_number in range(1, range_size):

#      for col_number in range(1, range_size):

#           number = row_number * col_number

#           print(f"{number}" , end="  " )

#           print()

import math

user_choice = int(input("How many columns and rows do you want in your multiplication table? "))

# Determine the maximum number in the table:
max_number = user_choice * user_choice

# Approach 1: Using an if statement
# digits = 2
# if max_number >= 100:
#     digits = 3 

# Approach 2: Computing the digits in math
# To find the number of digits, we want to know what power of 10 is this number (there is a
# mathematical operation to compute this called a logarithm).
# math.log10(25) is: 1.398
# math.log10(99) is: 1.996
# math.log10(100) is: 2.000

# Then, by converting it to an integer, it will drop the decimal part.
# Finally, we can then add 1 and we have the number of digits!

digits = int(math.log10(max_number)) + 1

# When we use range() in the loop below, it will go up to, but NOT INCLUDING the number
# so here we set the range_size to be the user's choice plus one.
range_size = user_choice + 1

# Iterate through that number of rows
for row_number in range(1, range_size):
    # For each for, we will also iterate through the same number of columns
    for col_number in range(1, range_size):
        # The number to display is the product of the row_number and the col_number
        number = row_number * col_number

        # Display the number with a space instead of a newline at the end: `end=" "`

        # This is a little tricky. If we just need the number 3, we could right:
        # print(f"{number:3}", end=" ")
        # But, since it is a variable number of digits, we have to put the variable name `digits`
        # inside of {}'s as well: {digits}
        print(f"{number:{digits}}", end=" ")
    
    # We have now printed all of the columns and are done with the row.
    # So it is now time to start a new line.
    print()

# import math

# user_input = int(input("How many number of rows and columns do you want in your multiplication table?"))
# the_maximum_number = user_input * user_input




     
     
    




#You now have code that can print out each column you'll need on a line. Now, you need to repeat it
#for a second line, and a third line, and so forth up until the number of rows that you need.
#To accomplish this, add another loop for each row that has your previous code as its body. 
#Start by simply having it duplicate the same row over and over again. Keep in mind that 
#you'll need to display a newline after the numbers for each row are finished.
#Then, once this is working change it to display the product of the row and column.
