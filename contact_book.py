contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts[name] = (phone, email, address)
    print("Contact added.")

def view_contacts():
    for name, (phone, _, _) in contacts.items():
        print(f"{name} - {phone}")

def search_contact():
    query = input("Search: ")
    for name, (phone, email, address) in contacts.items():
        if query in name or query in phone:
            print(f"Found: {name}, {phone}, {email}, {address}")

def update_contact():
    name = input("Update contact - Name: ")
    if name in contacts:
        print("Enter new details:")
        contacts[name] = (input("Phone: "), input("Email: "), input("Address: "))
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Delete contact - Name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    actions = {'1': add_contact, '2': view_contacts, '3': search_contact,
               '4': update_contact, '5': delete_contact}
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an action: ")
        if choice == '6':
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()