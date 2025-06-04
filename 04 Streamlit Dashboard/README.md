# 🔐 Password Generator App

This project is a **streamlined password generator** built with [Streamlit](https://streamlit.io/) that helps users generate secure and customizable passwords in three different styles:

- 🔢 **PIN codes**
- 🔐 **Random secure passwords**
- 🧠 **Memorable (human-friendly) passwords**

<img src="images/user-access.png" width="300" alt="User Access Image" style="display:block; margin:auto;" />

---

## 🚀 Features

- ✅ **PIN Code Generator**  
  Create numeric-only PINs of customizable length.

- ✅ **Random Password Generator**  
  Generate passwords with customizable length, including uppercase, lowercase, numbers, and special symbols.

- ✅ **Memorable Password Generator**  
  Create human-friendly passphrases using common English words, with options for separator and capitalization.

- ✅ **Interactive Streamlit UI**  
  Clean and easy-to-use interface with real-time password preview.

---

## 🖼️ App Preview

Here’s a screenshot of the Streamlit dashboard in action:

<p align="center">
  <img src="images/Screenshot 2025-06-04 235318.jpg" alt="Dashboard Preview" width="700"/>
</p>


## 🧰 Technologies Used

- Python 3.x
- [Streamlit](https://docs.streamlit.io/)
- [`wordfreq`](https://pypi.org/project/wordfreq/)
- Standard Python libraries: `random`, `string`, `abc`

---

## 📂 Project Structure
```
|--src
    |--dashboard.py
    |--password_generator.py   
|--README.md
|--requirements.txt
|--images
```
## 📦 Install Requirements
```bash
pip install -r requirements.txt
pip install streamlit wordfreq
```
## ▶️ Run the App
> Navigate to the project root directory:
```bash
streamlit run src/dashboard.py
```

---

## 🎯 Final Note

This app is designed to provide a **simple yet powerful interface** for generating secure passwords. Whether you need a quick PIN code, a complex random password, or a memorable passphrase, you can customize the output to fit your preferences.

🔧 Users can choose the password type, set the length, add symbols or numbers, and even adjust word separators and capitalization for memorable passwords — all through a clean and intuitive user interface.

A great user experience is at the heart of this project.  
**Good luck and happy coding! 🚀**



