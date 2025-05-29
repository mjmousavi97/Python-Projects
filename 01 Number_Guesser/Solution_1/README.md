# Number Guesser Game Project - Solution 1

## Description
This solution provides a modular approach to the Number Guesser Game. The game generates a random number between 1 and 100, and the user is prompted to guess this number. For each incorrect guess, the user receives a hint and their score is reduced.

## Directory Structure

```
number_guesser/Solution_1
|-- src/
| |-- game_logic/
| | |-- number_generator.py
| | |-- hint_generator.py
| |-- utils/
| | |-- input_validator.py
| |-- main.py
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## 🕹️ How to Play

1. Run the script using Python.
2. Enter a number between `1` and `100`.
3. Get feedback if your guess is:
   - Too low
   - Too high
   - Correct 🎉
4. Each wrong guess reduces your score by 10 points.
5. Type `q` to quit the game at any time.
6. After guessing correctly, you’ll be asked if you want to play again (`yes` or `no`).

## How to Run

1. Navigate to the main project directory (`Number_Guesser/Solution_1`).
2. Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```

Follow the on-screen prompts to play the game.

## Modules

- `src/main.py`: The main entry point of the game. It handles the game loop, user input, and display.
- `src/game_logic/`: Contains the core game logic.
  - `number_generator.py`: Generates a random number.
  - `hint_generator.py`: Provides hints based on the user's guess.
- `src/utils/`: Contains utility functions.
  - `input_validator.py`: Validates user input.


