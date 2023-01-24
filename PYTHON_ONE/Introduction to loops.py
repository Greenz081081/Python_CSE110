# Introduction to loops
# WEEK 07 / 08
#Lesson

# tip = float(input('What is the tipped amount?'))

# print(f"You have tipped an amount of ${tip:.2f}")

#What if the user decides to enter a negative number? 
# tip = float(input('What is the tipped amount?'))

# if (tip < 0):                  
#        print("Sorry the tip cannot be a nagative number")
#        tip = float(input('What is the tipped amount?'))
# if (tip < 0):                  
#        print("Sorry the tip cannot be a nagative number")
#        tip = float(input('What is the tipped amount?'))
# if (tip < 0):                  
#        print("Sorry the tip cannot be a nagative number")
#        tip = float(input('What is the tipped amount?'))
# if (tip < 0):                  
#        print("Sorry the tip cannot be a nagative number")
#        tip = float(input('What is the tipped amount?'))

# if (tip < 0):                  
#        print("Sorry the tip cannot be a nagative number")
#        tip = float(input('What is the tipped amount?'))

#        print(f"You have tipped an amount of ${tip:.2f}")
#Instead of using the long appication of if statements, we can easily use the "while" loop

# user = 8

# while (user < 10):                  
      
#        enter = int(input('What is the tipped amount?'))
    
      
#        print("You have tipped an amount")


#This also works when the computer is updating a value, rather than getting input from the user.
#The following program counts up to 5 and then stops:

# number = 1

# while (number <=5):
#       print(f"The number is:{number}")

#       number = number + 1
# print("Finished the loop")


number = 0

while number < 10:
       number = int(input("What is the number?")) 

print("Successful.")