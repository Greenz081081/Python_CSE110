# Week 07 team assignment
# Purpose: Create a Guess My Number Game
# Author: Emediong Edet
# import random

# magic_number = random.randint(1, 100)
# # question = int(input("What is the magic number?")) 
# guess = int(input("What your guess?")) 
# while guess < 100:
#     if (guess < 100):
#       print("Higher")
#       guess = int(input("What your guess?"))
#     # question = int(input("What is the magic number?")) 
#     # guess = int(input("What your guess?")) 

#     while guess > 100:
#       if (guess > 100):
#           print("Lower")
#           guess = int(input("What your guess?"))
#         #   question = int(input("What is the magic number?")) 
#     # guess = int(input("What your guess?")) 


# if (guess == 100):
#     print("You guessed it")
#     print("Game Over")





# else:
#               print("Invalid \nretry")
    

# magic_number = 0
# question = int(input("What is the magic number?")) 
# guess = int(input("What your guess?")) 
# if (guess < 6):
#      question = int(input("What is the magic number?")) 
#      guess = int(input("What your guess?")) 
#      print("Higher")
# else:
#     print("Invalid \nRetry")

#     if (guess > 6):
#         question = int(input("What is the magic number?")) 
#         guess = int(input("What your guess?"))
#         print("Lower")
#     else:
#         print("Invalid \nRetry")   

#         if (guess > 6):
#          question = int(input("What is the magic number?")) 
#          guess = int(input("What your guess?"))
#          print("You guessed it")
#         else:
#             print("Invalid \nRetry") 
animal = "dog"
while animal == "dog":
   print("a")
   animal = "cat"
   print("b")
print("c")

      
# guess = 0

# while guess < 18 \
#      or guess > 18: 
#  question = int(input("What is the magic number?")) 
#  guess = int(input("What your guess?"))
#  print("Higher")




        
# print("You guessed it!")



# The correct way to write the program using the instructor's guide.

#import random


#magic_number = random.randint(1, 100)

# I need to start the variable "guess" at something, but I don't want to start it as
# valid number that the computer may have chosen, so I'll start with -1

#guess = -1

# Keep going as long as the guess doesn't match the magic number

# while guess != magic_number:
#     guess = int(input("What is your guess?"))

#     if guess < magic_number:
#         print("Higher")
#     elif guess > magic_number:
#         print("Lower")
#     else:
#         print("You guessed it!")
 
#Guess my number game, including the stretch challenges.
#import random

#keep_playing = "Yes"

#As long as they say "yes" we will keep playing
#while keep_playing == "yes":
    #magic_number = random.randint(1, 100)

#this variable will keep track of how many guesses it took

#guess_count = 0

#guess = -1

#Keep going as long as the guess doesn't match the magic number

# while guess != magic_number:
#     guess = int(input("What is your guess?"))
#     guess_count = guess_count + 1

#     if guess < magic_number:
#         print("Higher")
#     elif guess > magic_number:
#         print("Lower")
#     else:
#         print("You guessed it!")


#At this point, they have guessed it correctly

# print(f"It took you {guess_count} guesses")

# keep_playing = input("Do you want to keep playing (Yes/No)")

# print("Game Over \n Thank you for playing, Goodbye!")
