import json
import os

FILE = "contacts.json"  

def load_contacts():
    if not os.path.exists(FILE):
        return {}  # If JSON file does not exist, return empty dictionary
    with open(FILE, "r") as f:
        return json.load(f)  # Load data from contacts.json

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added!")

def update_contact(contacts):
    name = input("Enter contact name to update: ")

    if name not in contacts:
        print("Contact not found!")
        return

    phone = input("New phone number: ")
    email = input("New email: ")

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact updated!")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted!")
    else:
        print("Contact not found!")

def search_contact(contacts):
    name = input("Enter name to search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("No contact found.")

def main():
    contacts = load_contacts()     # <--- Load data from JSON here

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            update_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid option!")


main()
