# 🔐 Password Generator - Functional Implementation (Solution B)

This solution provides a clean, straightforward implementation of a password generation system using **pure functional programming techniques** in Python.

It is part of a comparative project that demonstrates solving the same problem with two different paradigms: object-oriented (Solution A) and functional (Solution B).

---

## 📚 Overview

This functional approach includes three standalone functions, each responsible for generating a different type of password:

- **`generate_pin()`** – Generates a numeric-only PIN
- **`generate_random_password()`** – Creates random character-based passwords
- **`generate_memorable_password()`** – Produces readable passwords using vocabulary words

Each function is self-contained, easily testable, and does not rely on any shared object state.

---

## 📁 Folder Structure

```
|--solution B   
    |--src   
        |--main.py   
    |--README.md  
    |--requirements.txt    
```
## 🛠️ Technologies Used

- **Python 3.8+**
- **External Library**: 
> No external libraries are required unless you provide a custom vocabulary for the memorable password generator.


---
## ▶️ How to Run
Navigate to the project root (where src/ is located):
```bash
python src/main.py
```
