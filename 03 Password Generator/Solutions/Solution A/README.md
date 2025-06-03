# 🔐 Password Generator - Object-Oriented Implementation (Solution A)

This solution implements a flexible, extensible password generation system using **Object-Oriented Programming (OOP)** principles in Python.

It is part of a larger comparison project that demonstrates different programming paradigms for solving the same problem (i.e., password generation). This specific folder contains the OOP-based solution.

---

## 📚 Overview

In this implementation, we define a common interface (`PasswordGenerator`) and derive three concrete classes:

1. **`PinGenerator`** – for numeric-only PINs  
2. **`RandomPasswordGenerator`** – for secure random character-based passwords  
3. **`MemorablePasswordGenerator`** – for readable, phrase-like passwords using common English words  

Each class implements the `generate()` method in its own way while adhering to the shared abstract base class.

---

## 🧱 Folder Structure
```   
|--solution A   
    |--src   
        |--main.py   
    |--README.md 
    |--requirements.txt 
```

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **External Library**: [`wordfreq`](https://pypi.org/project/wordfreq/)
    - Used for fetching a list of common English words for memorable password generation.

---

## 🚀 Installation

Install the required package using pip:

```bash
pip install wordfreq
```
## ▶️ How to Run
Navigate to the project root (where src/ is located):
```bash
python src/main.py
```
