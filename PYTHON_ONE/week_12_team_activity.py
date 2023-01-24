# # week 12 team activity
# # In this activity, you will practice finding items in a file. 
# # You will be supplied with a file that contains the books in 
# # The Standard Works of the Scriptures, and for each book the number of chapters.
# # You will need to open this file, parse through it, and discover books that have certain properties. 
max_chapters = -1
books_with_max = ""
with open("books_and_chapters.txt") as books_file:

    for line in books_file:
       

        parts = line.split(":")

# Open the file, read through it line by line, separate the line into the appropriate 
# pieces and display each book in this format:
# Scripture: Old Testament, Book: Genesis, Chapters: 50

        book = (parts[0]).strip()

        chapters = int(parts[1])

        scripture = parts[2].strip()


        print(f"Scripture: {scripture}, Book: {book}, Chapter: {chapters}")

# Find the largest number of chapters in the scriptures.
# Find the book that has the largest number of chapters in the scriptures.

        if chapters > max_chapters:

            max_chapters = chapters
            books_with_max = book

        

print(f"The book with the most chapters is: {books_with_max}")
print(f"It has {max_chapters} chapters.")







