def myContacts():
    lists = []

    while True:
        print("\nMy Contacts")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                name = input("Enter contact name: ")
                lists.append(name)
                print("Contact added!")
            except:
                print("Error adding contact.")

        elif choice == "2":
            try:
                if len(lists) == 0:
                    print("No contacts to remove.")
                    continue

                print("\nContacts List:")
                for i, c in enumerate(lists):
                    print(f"{i + 1}. {c}")

                index = int(input("Enter contact number to remove: "))

                if 1 <= index <= len(lists):
                    removed = lists.pop(index - 1)
                    print(f"{removed} removed.")
                else:
                    print("Invalid contact number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

myContacts()
