import json
import os

DATA_FILE = "locker_data.json"

# Load locker data if exists
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"pin": None, "items": []}

# Save locker data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Register or login
def authenticate(data):
    if data["pin"] is None:
        pin = input("Set your 4-digit PIN: ")
        data["pin"] = pin
        save_data(data)
        print("Locker created successfully!\n")
    else:
        while True:
            pin = input("Enter your PIN: ")
            if pin == data["pin"]:
                print("Access granted!\n")
                break
            else:
                print("Incorrect PIN. Try again.")

# Menu for locker options
def locker_menu(data):
    while True:
        print("1. Add Item")
        print("2. View Items")
        print("3. Remove Item")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            item = input("Enter item to store: ")  
            data["items"].append(item)
            save_data(data)
            print("Item added successfully!\n")

        elif choice == "2":
            print("\nStored Items:")
            for i, item in enumerate(data["items"], start=1):
                print(f"{i}. {item}")
            print()

        elif choice == "3":
            num = int(input("Enter item number to remove: ")) - 1
            if 0 <= num < len(data["items"]):
                removed = data["items"].pop(num)
                save_data(data)
                print(f"Removed: {removed}\n")
            else:
                print("Invalid number.\n")

        elif choice == "4":
            print("Exiting locker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Main program
def main():
    data = load_data()
    authenticate(data)
    locker_menu(data)

if __name__ == "__main__":
    main()
