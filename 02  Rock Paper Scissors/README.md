# 🪨 Rock Paper Scissors Game

A simple command-line **Rock, Paper, Scissors** game built with Python, using clean object-oriented programming (OOP) principles.

This game allows a player to play multiple rounds against the computer, with clear feedback and winner announcements each time.

---

## 📌 Project Features

- Simple and interactive command-line interface
- Clean OOP structure using a `RockPaperScissors` class
- Input validation to ensure correct choices
- Random computer opponent
- Replay loop (play again until you quit)

## 📂 Project Structure
``` 
02 Rock Paper Scissors/   
   |-- src/    
        |-- game.py     
   |-- README.md
   |-- requirements.txt
```

## 🕹️ How to Play

1. When the game starts, you’ll be asked to choose one of:
   - `rock`
   - `paper`
   - `scissors`

2. The computer will randomly select its own move.

3. The game determines the winner based on classic rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock

4. The result of the round (win/loss/tie) is printed.

5. You will be asked if you want to play again. Enter:
   - Any key to **continue**
   - `q` or `Q` to **quit**


## 💻 How to Run

Navigate to the project directory, then run the game using the following command:
   ```bash
   python src/game.py
