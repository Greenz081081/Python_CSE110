# Task: Open files in python
# purpose: Use programming building blocks

# Download the file books.txt that contains the names in the Book Of Mormon, 
# and save it to your computer
# Once you have the file saved to your computer, in VS Code, open the folder that contains it
# and create a new script.


# Open the file
# The "wiht" syntax makes it so I don't have to worry about closing it later
with open("books.txt") as books_file:


# Go through each line in the file, one by one
    for book in books_file:
# The .strip() function returns a new line that doesn't have leading or trailing whitespace.
# In other words,it strips off the "\n" that
# would otherwise be at the end of each line.
        book = book.strip()
 # print the book out to the screen       
        print(book)

print()
print("The file is closed now")