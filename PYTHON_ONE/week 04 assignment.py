# File: week 03 assignment
# Purpose: write a program to calculate the price of a meal.
# Author: Emediong Edet
print()
print("Please enter the following informations:")
print()
childs_meal = float(input("What is the price of a child's meal?" ))
adults_meal = float(input("What is the price of an adult's meal?"))
childs_appetizer = float(input("What is the price of a child's appetizer?"))
childs_drink = float(input("What is the price of a child's drink?"))
adults_drink = float(input("What is the price of an adult's drink"))
adults_appetizer = float(input("What is the price of an adult's appetizer?"))
number_of_children = int(input("How many children are there?"))
number_of_adults = int(input("How many adults are there?"))
sales_tax_rate = float(input("What is the sales tax rate?"))
print()
print()
subtotal_1 = (childs_meal + childs_appetizer + childs_drink) * number_of_children
subtotal_2 = (adults_meal + adults_appetizer + adults_drink) * number_of_adults
Subtotal = subtotal_1 + subtotal_2
print()
print(f"Subtotal: ${Subtotal:.2f}")
sub_sales_tax = Subtotal * ( sales_tax_rate /  100 )  
Sales_Tax = sub_sales_tax
print(f"Sales Tax: ${Sales_Tax:.2f}")
sub_total = Subtotal + Sales_Tax
Total = sub_total
print(f"Total: ${Total:.2f}")
print()
payment_amount = float(input("What is the payment amount?"))
sub_change = payment_amount - Total
Change = sub_change
print(f"Change: ${Change:.2f}")
end = input("..")