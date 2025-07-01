from collections import defaultdict
from typing import Optional, Dict


class ContactBook:
    """
    A simple contact book to store and manage contacts with their phone, email, and national ID.
    """

    def __init__(self) -> None:
        """
        Initializes the ContactBook with an empty contacts dictionary.
        """
        self.contacts: Dict[str, Dict[str, Optional[str]]] = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: Optional[str] = None, id: Optional[str] = None) -> None:
        """
        Adds a new contact to the contact book.

        :param name: Name of the contact.
        :param phone: Phone number of the contact.
        :param email: Email address of the contact (optional).
        :param id: National ID of the contact (optional).
        """
        if name in self.contacts:
            print("Contact Already Exists")
            return
        
        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email
        self.contacts[name]['id'] = id

    def view_contacts(self) -> None:
        """
        Prints all contacts stored in the contact book.
        """
        for name, info in self.contacts.items():
            email = info['email'] if info['email'] is not None else "N/A"
            nid = info['id'] if info['id'] is not None else "N/A"
            print(f"Name: {name}, Phone: {info['phone']}, Email: {email}, National_ID: {nid}")
            print('-' * 100)

    def delete_contact(self, name: str) -> None:
        """
        Deletes a contact by name.

        :param name: Name of the contact to delete.
        """
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    def update_contact(self, name: str, phone: Optional[str] = None, email: Optional[str] = None, id: Optional[str] = None) -> None:
        """
        Updates an existing contact's information.

        :param name: Name of the contact to update.
        :param phone: New phone number (optional).
        :param email: New email address (optional).
        :param id: New national ID (optional).
        """
        if name in self.contacts:
            if phone is not None:
                self.contacts[name]['phone'] = phone
            if email is not None:
                self.contacts[name]['email'] = email
            if id is not None:
                self.contacts[name]['id'] = id
            print("Contact updated successfully!")
        else:
            print("Contact not found!")


if __name__ == '__main__':
    book = ContactBook()

    while True:
        print("\n=== Contact Book ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email (optional): ") or None
            nid = input("National ID (optional): ") or None
            book.add_contact(name, phone, email, nid)
        
        elif choice == '2':
            book.view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            phone = input("New Phone (leave empty to skip): ") or None
            email = input("New Email (leave empty to skip): ") or None
            nid = input("New National ID (leave empty to skip): ") or None
            book.update_contact(name, phone, email, nid)
        
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            book.delete_contact(name)

        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
