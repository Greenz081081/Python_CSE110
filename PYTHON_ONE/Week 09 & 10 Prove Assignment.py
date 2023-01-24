# Week 09 Prove Assignment

# For this project you will create a program that stores a list of products in a shopping cart along with their prices. 
# The user should have the ability to add items to the list, remove them, and see the total price of the carts


option = None
user_choice = None
carts = []
# Store prices as well as names.
prices = []
price = None
item_index = None



options = "Add a new item", "Display contents", "Remove an item", "Compute total", "Display quantity", "quit"

menus = ["1. Add a new item", "2. Display contents", "3. Remove an item", "4. Compute total", "5. Display quantity", "6. quit"]
print("Welcome to the shopping cart program!")

print()
print("Please select one of the following:")

#Display the menu to the user. 
for menu in menus:
   print(menu) 


print()
# A while loop that would continue looping until the user chooses the quit option.
while option != "6":
  option = input("Please enter an option:")

  if option == "1":
# Add an item to the list.
    print()
    user_choice = input("What item would you like to add?")
    # Change the add functionality to also ask for and store the price of the item.
    price = float(input(f"What is the price of {user_choice}?"))
    carts.append(user_choice)
    prices.append(price)
    print(f" '{user_choice}' has been added to the cart.")

    print()
    print("Please select one of the following:")
    for menu in menus:
      print(menu)
   

# Display contents
  elif option == "2":

  # When displaying the items, display a number in front of each item. The numbers should start with 1.
    print()
    print("The contents of the cart are:")
    for i in range(len(carts)):
      user_choice = carts[i] 
      price = prices[i]
      print(f"{i + 1}. {carts[i]:15} - ${prices[i]:.2f}")
     


    print()
    print("Please select one of the following:")
# Repeat the menu until the user chooses quit.
    for menu in menus:
      print(menu)

  elif option == "3":
  # Complete the option to remove an item from the shopping cart.
    print()
    item_index = int(input("Which item would you like to remove?"))
    carts.pop(item_index -1)
    prices.pop(item_index -1)
    print("Item removed")
    

  elif option == "4":
    
    sum = 0

    print()
    for price in prices:
         sum += price
    print(f"The total price of the items in the shopping cart is: ${sum:.2f}")
    print()


    print()
  elif option == "5":
    length = (len(carts))
    print(f"There are {length} items on your list.")
    print()




  elif option == "6":
      print("Thank you for your choices. Goodbye.")
# Display an invalid command to the user when the user makes a wrong choice.
  else:
      print("Invalid Command!") 
      