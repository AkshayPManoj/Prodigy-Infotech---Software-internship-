import json

# Global variable to store contacts
contacts = []

def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(index, name, phone, email):
    if 0 < index <= len(contacts):
        contacts[index - 1] = {"name": name, "phone": phone, "email": email}
        print("Contact edited successfully!")
    else:
        print("Invalid contact index.")

def delete_contact(index):
    if 0 < index <= len(contacts):
        del contacts[index - 1]
        print("Contact deleted successfully!")
    else:
        print("Invalid contact index.")

def save_contacts_to_file(filename):
    with open(filename, "w") as file:
        json.dump(contacts, file)
    print("Contacts saved to file successfully!")

def load_contacts_from_file(filename):
    global contacts
    try:
        with open(filename, "r") as file:
            contacts = json.load(file)
        print("Contacts loaded from file successfully!")
    except FileNotFoundError:
        print("Contacts file not found.")

def main():
    filename = "contacts.json"  # File to store contacts
    load_contacts_from_file(filename)
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            index = int(input("Enter index of contact to edit: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            edit_contact(index, name, phone, email)
        elif choice == "4":
            index = int(input("Enter index of contact to delete: "))
            delete_contact(index)
        elif choice == "5":
            save_contacts_to_file(filename)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
