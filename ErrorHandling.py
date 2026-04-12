def withdrawal_system():
    balance = 5000

    while True:
        print("\n=== Money Withdrawal System ===")
        print("1. Withdraw Money")
        print("2. Check Balance")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to withdraw: "))

                if amount <= 0:
                    print("Error: Please enter a valid positive amount.")
                    continue

                if amount > balance:
                    print("Error: Insufficient funds.")

                   
                    while True:
                        print("\nWhat would you like to do?")
                        print("1. Try Again")
                        print("2. Check Balance")
                        print("3. Exit")

                        option = input("Choose an option: ")

                        if option == "1":
                            break
                        elif option == "2":
                            print(f"Current Balance: {balance}")
                        elif option == "3":
                            print("Exiting program...")
                            return
                        else:
                            print("Invalid choice. Try again.")
                else:
                    balance -= amount
                    print(f"Withdrawal successful!")
                    print(f"Remaining Balance: {balance}")

            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")

        elif choice == "2":
            print(f"Current Balance: {balance}")

        elif choice == "3":
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
withdrawal_system()
