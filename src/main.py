# به نام خدا
# author: AliMHD

from tabulate import tabulate


class ContactBook:
    """
    A class used to represent a Contact Book.
    """
    def __init__(self):
        """
        Initialize contact book object with an empty dictionary.
        """
        self.contacts: dict = {}

    def add_contact(self, name: str, phone: str, email: str, address: str):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("Contact added successfully!")
        else:
            print("Contact already exists.")

    def view_contacts(self):
        """
        Displays all contacts in the contact book.
        """
        table = []
        for name, info in self.contacts.items():
            table.append([name, info["phone"], info["email"], info["address"]])
        headers = ["Name", "Phone", "Email", "Address"]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def delete_contact(self, name: str):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found")

    def edit_contact(self, name: str, phone: str = None, email: str = None, address: str = None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print("Contact updated successfully!")
            return
        print("Contact not found")
    
    


if __name__ == "__main__":
    book = ContactBook()

    def show_menu():
        menu = [
            ["1", "Add contact"],
            ["2", "Edit contact"],
            ["3", "View contacts"],
            ["4", "Delete contact"],
            ["5", "Quit"],
        ]

        print(tabulate(menu, headers=["Option", "Description"], tablefmt="rounded_grid"))

    while True:
        print("\n--- Contact Book Application ---")
        show_menu()
        user_choice = input("\nPlease choose an option: ")

        if user_choice == '1':
            name = input("\nEnter Contact name: ")
            phone = input("Enter Contact phone: ")
            email = input("Enter Contact email: ")
            address = input("Enter Contact address: ")
            book.add_contact(name, phone, email, address)

        elif user_choice == '2':
            name = input("\nEnter name of the contact to edit: ")
            phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
            email = input("Enter new/updated email or press Enter to keep unchanged: ")
            address = input("Enter new/updated address or press Enter to keep unchanged: ")
            book.edit_contact(name, phone or None, email or None, address or None)

        elif user_choice == '3':
            print("\nList of Contacts:")
            book.view_contacts()

        elif user_choice == '4':
            name = input("\nEnter name of contact to delete: ")
            book.delete_contact(name)

        elif user_choice == '5':
            print("\nThank You for using Contact Book Application. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")
