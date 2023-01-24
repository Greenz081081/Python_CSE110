# 10 Teach: Team Activity
# Multiple Lists

# Sometimes you have two lists that you 
# want to keep in sync with each other. For example, in this assignment, 
# you will track bank accounts and the balances in each one.

print("Enter the names and balances of bank accounts (type: quit when done)")
#Create two lists, one for the names of the bank accounts, and one for the balances.
bank_account_names = [] 
bank_account_balances = []
user_bank_name = None
user_bank_account_balance = None
update = "yes"

# Ask the user for the name of the bank account and then for its current balance.
# Keep looping until the user types "quit" for the name of an account.
# For each one, add the name and the balance to the appropriate list. 
while user_bank_name != "quit":
    user_bank_name = input("What's the name of this account?")

    if user_bank_name != "quit":
        user_bank_account_balance = float(input("What's the current balance?"))
        # print("Your account names are:")
        bank_account_names.append(user_bank_name)
        bank_account_balances.append(user_bank_account_balance)


# Loop through the lists using an index and display the name of the account with the balance next to it.
print()
print("Account Information:")
for i in range(len(bank_account_names)):
    bank_account_name = bank_account_names[i]
    bank_account_balance = bank_account_balances[i]
   #  print("{:<25}".format(i))
   #  print("{:<25}".format(bank_account_name))
   #  print("{:>25}".format(bank_account_balance))

    # Change your display so that it shows the index of the account next to the name.
    print(f"{i}. {bank_account_name} - ${bank_account_balance:.2f}")



# Compute and display the total balance in all of the accounts and the average balance.
sum = 0

print()
for bank_account_balance in bank_account_balances:
   sum += bank_account_balance
print(f"Total: ${sum}")

length = len(bank_account_balances)



average = sum / length

print(f"Average: ${average:.2f}")

# STRETCH CHALLENGE

# Determine which bank account has the highest balance and display the name and balance of that account.
# Change your display so that it shows the index of the account next to the name.


highest = -1

for bank_account_balance in bank_account_balances:

   if bank_account_balance > highest:

      highest = bank_account_balance

print(f"Highest Balance: {bank_account_name} - ${bank_account_balance:.2f}")

# After displaying the list, ask the user if they want to update an account.
# If they respond with yes, ask for the index of the account, and the new balance.

print()
while update == "yes":
   update = input("Do you want to update an account?")

   if update == "yes":
      account_index = int(input("What account index do you want to update?"))
      new_amount = float(input("What is the new amount?"))
   
# bank_account_balances[account_index] = new_amount

# Change the last step into a loop, so that the user can keep 
# updating accounts until they say no. After each update, display the new list of balances.
   # if update == "yes":
      bank_account_balances[account_index] = new_amount

      print()
      print("Account Information:")
      for i in range(len(bank_account_names)):
         bank_account_name = bank_account_names[i]
         bank_account_balance = bank_account_balances[i]
         print(f"{i}. {bank_account_name} - ${bank_account_balance:.2f}")

         sum = 0

      print()
      for bank_account_balance in bank_account_balances:
         sum += bank_account_balance
      print(f"Total: ${sum}")

      length = len(bank_account_balances)



      average = sum / length

      print(f"Average: ${average:.2f}")

            

      # highest = -1

      # for bank_account_balance in bank_account_balances:

      #    if bank_account_balance > highest:

      #       highest = bank_account_balance

      # print(f"Highest Balance: {bank_account_name} - ${bank_account_balance:.2f}")

   print()
        










 