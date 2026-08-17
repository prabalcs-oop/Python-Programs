contacts ={}

while True:
    print("\n-- CONTACT BOOK---")
    print("1.Add contact:")
    print("2.View contacts")
    print("3.Search contact")
    print("4.Delete contact")
    print("5.Exit")

    choice = input("Choose:")

    if choice == "1":
        name = input("Name:").strip()
        phone = input("Phone:").strip()
        contacts[name] = phone
        print("Contact saved.")

    elif choice == "2":
        if not contacts:
            print("No contacts.")
        else:
            for name,phone in contacts.items():
                print(f"{name}:{phone}")

    elif choice =="3":
        name = input("Enter name:").strip()
        print(contacts.get(name,"contact not found"))

    elif choice =="4":
        name=input("Enter name:").strip()
        if contacts.pop(name,None) is not None:
            print("Contact deleted!")
        else:
            print("Contact not found.")

    elif choice == "5":
        break

    else:
        print("Invalid option.")                               