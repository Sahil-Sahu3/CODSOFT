
contacts = []

def add_contact():
    print("\n------Add new Contact------")

    name = input("Enter Name:")
    phone = input("Enter phone number:")
    email = input("Enter Email:")
    address = input("Enter address:")

    contact = {
       "name" : name,
       "phone" : phone,
       "email" : email,
       "address" : address 
    }

    contacts.append(contact)
    print("CONTACT ADDED SUCCESSFULLY")

def view_contact():
    print("\n----Contact List----")

    if not contacts:
        print("---No Contacts Found---")
        return
    
    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

def search_contact():
    key = input("Enter the contact you want to search:")

    found = False
    for contact in contacts:
        if key.lower() in contact["name"].lower() or key in contact["phone"]:
            print("---CONTACT FOUND---")
            for field in contact:
                print(field, contact[field])
            found = True
            break
    if not found:
        print("CONTACT DOES NOT EXIST")

def update_contact():
    print("\n---UPDATE CONTACT---")

    name_to_update = input("Enter the name you want to update:")
    for contact in contacts:
        if contact["name"].lower() == name_to_update:
            print("Leave blank by to keep the current information")
        new_name = input("New name(or press enter to keep current):")
        new_phone = input("New phone number:")
        new_email = input("New email:")
        new_address = input("New address: ")

        if new_name:
            contact["name"] = new_name
        if new_phone:
            contact["phone"] = new_phone
        if new_email:
            contact["email"] = new_email
        if new_address:
            contact["address"] = new_address   

        print("CONTACT UPDATED SUCCESSFULLY")
        return
    print("CONTACT NOT FOUND") 

def delete_contact():
    print("\n---DELETE CONTACT---")

    name_to_delete = input("Enter the name of the contact you want to delete:")

    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name_to_delete.lower():
            confirm = input(f"Are you sure you want to delete {contact['name']}? (yes/no): ").lower()
            if confirm == "yes":
                contacts.pop(i)
                print(" Contact deleted.")
            else:
                print(" Deletion cancelled.")
            return

    print(" Contact not found.")

def show_menu():
    while True:
        print("\n=======CONTACT BOOK=========")
        print("1. Add Contact")
        print("2. View all Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6):") 
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print(" Goodbye! Thank you for using Contact Book.")
            break
        else:
            print(" Please enter a valid choice (1-6).")

show_menu()  



