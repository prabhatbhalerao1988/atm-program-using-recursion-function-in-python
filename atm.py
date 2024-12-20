print("...Welcome to the ATM!...")

bal = 1000

# Define the recursive ATM function
def atm_menu():
    global bal  # To access and modify the global balance variable
    
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    c = input("Enter your choice (1/2/3/4): ")

    match c:
        case '1':
            print(f"Your current balance is: Rs{bal}")

        case '2':
            deposit_amount = float(input("Enter amount to deposit: Rs"))
            if deposit_amount > 0:
                bal=bal+deposit_amount
                print(f"Deposited Rs{deposit_amount}. Your new balance is: Rs{bal}")
            else:
                print("Invalid deposit amount. Please try again.")
        
        case '3':
            withdraw_amount = float(input("Enter amount to withdraw: Rs"))
            if withdraw_amount > 0 and withdraw_amount <= bal:
                bal=bal-withdraw_amount
                print(f"Withdrew Rs{withdraw_amount}. Your new balance is: Rs{bal}")
            elif withdraw_amount > bal:
                print("Insufficient funds! Please enter a smaller amount.")
            else:
                print("Invalid withdrawal amount. Please try again.")
        
        case '4':
            print("Thank you for using the ATM. Goodbye!")
            return  # Exit the recursion and end the program
        
        case _:
            print("Invalid choice. Please enter a number between 1 and 4.")

    # Recursively call the function to show the menu again if not choosing '4'
    atm_menu()

# Call the recursive function to start the program
atm_menu()
