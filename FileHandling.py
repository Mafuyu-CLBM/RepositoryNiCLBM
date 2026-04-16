filename = "message.txt"

try:
    file = open(filename, "x")
    print("File created successfully!")
    file.close()
except FileExistsError:
    print("Error: File already exists.")

# Function to display menu
def menu():
    while True:
        print("\n--- Simple Messaging App ---")
        print("1. Send a message")
        print("2. View all messages")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # Send message (append)
        if choice == "1":
            try:
                message = input("Enter your message: ")
                with open(filename, "a") as file:
                    file.write(message + "\n")
                print("Message saved!")
            except Exception as e:
                print("Error writing to file:", e)

        # View messages (read)
        elif choice == "2":
            try:
                with open(filename, "r") as file:
                    print("\n--- Messages ---")
                    content = file.read()
                    if content:
                        print(content)
                    else:
                        print("No messages yet.")
            except Exception as e:
                print("Error reading file:", e)

        # Exit
        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
