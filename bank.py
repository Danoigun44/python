# creating a login and interactive account ledger
account_holder = input("Enter the account holder's name: ")
balance = 0.0
while True:
   print("\nBanking System Menu:")
   print("1. Check Balance")
   print("2. Deposit Money")
   print("3. Withdraw Money")
   print("4. Exit")
   choice = input("Choose an option: ")
   if choice == "1":
       # Check Balance
       print(f"Account holder: {account_holder}")
       print(f"Current balance: ${balance:.2f}")
   elif choice == "2":
       # Deposit Money
       amount = float(input("Enter amount to deposit: "))
       if amount > 0:
           balance += amount
           print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
       else:
           print("Deposit amount must be positive.")
   elif choice == "3":
       # Withdraw Money
       amount = float(input("Enter amount to withdraw: "))
       if amount > 0:
           if balance >= amount:
               balance -= amount
               print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
           else:
               print("Insufficient balance.")
       else:
           print("Withdrawal amount must be positive.")
   elif choice == "4":
       # Exit
       print("Exiting banking system. Thank you!")
       break
   else:
       print("Invalid option. Please try again.")
