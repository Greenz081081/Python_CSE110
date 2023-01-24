# Week 10 Checkpoint Activity
# Purpose: Practice Working With List Indexes

shopping_lists = []
item = None

# Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."
print("Please enter the items of the shopping list (type: quit to finish)")
print()
# Loop through the items in the regular way (for example, for thing in the_list)
# and display each one to make sure you have the initial list built correctly.
while item != "quit":
      item = input("Item:")
  

      if item != "quit":
        shopping_lists.append(item)


print()
print("The contents of the list are:")


for item in shopping_lists:
     print(item)


print()
print("The shopping list with indexes is:")

# Add another loop to go through and print the items in the list, but this time,
# instead of using the for ... in syntax, use an index (for example, for ... in range)
# and then access the item using the index and the square brackets. Print the index in 
# front of the items like so: 0. Milk



for i in range(len(shopping_lists)):
      shopping_list = shopping_lists[i]
      print(f"{i}. {shopping_list}")


# Ask the user for an index and a new shopping list item.
# Replace the item at that index with the new item. Then, display the whole list again.

item_change = int(input("Which item would you like to change?")) 
new_item = input("What is the new item?")

shopping_lists[item_change] = new_item



print()
print("The shopping list with indexes is:")

for i in range(len(shopping_lists)):
      shopping_list = shopping_lists[i]
      print(f"{i}. {shopping_list}")

