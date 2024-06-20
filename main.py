from contact import *
print("*** CONTACT BOOK ****")
print()
def main():
    contact_book = ContactBook()
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.update_contact()
        elif choice == "4":
            contact_book.delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
