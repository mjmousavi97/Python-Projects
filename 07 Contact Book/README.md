# 📒 Contact Book CLI

A simple yet powerful Python command-line interface (CLI) application to store, manage, and manipulate contacts with their phone numbers, emails, and national IDs.

This project demonstrates a minimal implementation of a contact book using Python OOP principles, complete with type hints and Sphinx-style docstrings.

---

## 🚀 Features

✅ Add new contacts with name, phone, email, and national ID  
✅ View all stored contacts in a structured format  
✅ Update existing contact information  
✅ Delete contacts by name  
✅ Easy-to-use command-line interface (CLI)  
✅ Type annotations for better code safety  
✅ Well-documented with Sphinx-style docstrings

---

## ⚙️ Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/mjmousavi97/Python-Projects.git
cd Python-Projects/07\ Contact\ Book
```
## 📌 Usage
Simply run the main.py file with Python:
```bash
python src/main.py
```
You will see a menu like:

=== Contact Book ===
1. Add contact
2. View contacts
3. Update contact
4. Delete contact
5. Exit

Then follow the prompts to add, view, update, or delete contacts.

## 📝 Usage Examples
➕ Adding a contact
```bash
Enter your choice: 1
Name: Mohammad Javad
Phone: 09350676685
Email (optional): mj.mousavi@ut.ac.ir
National ID (optional): 0560070586
```
📃 Viewing contacts
```bash
Enter your choice: 2
Name: Mohammad Javad, Phone: 09350676685, Email: mj.mousavi@ut.ac.ir, National_ID: 0560070586
----------------------------------------------------------------------------------------------------
```
✏️ Updating a contact
```bash
Enter your choice: 3
Enter the name of the contact to update: Mohammad Javad
New Phone (leave empty to skip):
New Email (leave empty to skip):
New National ID (leave empty to skip): 0569973864
Contact updated successfully!
```
🗑️ Deleting a contact
```bash
Enter your choice: 4
Enter the name of the contact to delete: Mohammad Javad
Contact deleted successfully!
```

📦 Requirements

> Python 3.7+
___

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
___

📬 Contact

Made with ❤️ by Mohammad Javad