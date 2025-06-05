# 😊 Happy Number Checker

This is a simple and interactive **Streamlit** web app that checks whether a given number is a *happy number* or not.

---

## 📌 What is a Happy Number?

A **happy number** is defined by the following process:

> Starting with any positive integer, replace the number by the **sum of the squares of its digits**, and repeat the process. If the process ends in 1, then the number is considered *happy*. Otherwise, it enters a loop and is *not happy*.

## 💡 Features
Friendly UI with emojis 😄

Mathematical explanation for happy numbers 🧮

Lightweight and easy to run 💻

Built-in unit testing ✅

## **Example:**
```
19 → 1² + 9² = 1 + 81 = 82
82 → 8² + 2² = 64 + 4 = 68
68 → 6² + 8² = 36 + 64 = 100
100 → 1² + 0² + 0² = 1 ✔️ (Happy!)
```


---

## 📁 Project Structure
```
|--src
    |--dashboard.py
    |--main.py
|--README.md 
|--requirements.py
|--images
```


## 🧪 Unit Tests
```bash
python src/main.py
```
If all is correct:
```bash
All test cases pass
```

## 🚀 How to Run
Make sure the src directory is on the Python path:
```bash 
export PYTHONPATH=.
```
Run the Streamlit app:
```bash
streamlit run src/dashboard.py
```

---

### 🙌 Final Note

Let’s make the world happier, one number at a time!  
Thank you for visiting this project — your curiosity keeps numbers smiling 😊


