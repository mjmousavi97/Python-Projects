import random

def validate_input(user_guess):
    """_summary_

    :param user_guess: _description_
    :type user_guess: _type_
    :return: _description_
    :rtype: _type_
    """
    if not user_guess.isdigit():
        print("Invalid input. Please try again!")
        return False
    
    user_guess = int(user_guess)
    if user_guess > 100 or user_guess < 1:
        print("Your guess is out of range. Please try again. Your should be in range 1 to 100.")
        return False
    
    return True


def show_instructions():
    """
    Show the welcome message and instructions to the user.
    """
    print("Welcome to the Number Guessing Game!")
    print("I have picked a random number between 1 and 100.")
    print("Your goal is to guess it.")
    print("After each guess, I'll tell you if your guess is too high or too low.")
    print("You start with 100 points and lose 10 points for each wrong guess.")
    print("Type 'q', 'quit', or 'exit' anytime to leave the game.")
    print("Let's start!\n")


def main():
    """
    Main function to run the number guessing game.

    This function generates a random number between 1 and 100, keeps track
    of the user's score, handles user input, validates guesses, gives
    feedback, and manages the replay logic. The game continues until the
    user decides to quit by typing 'q', 'exit', or 'quit'.
    """
    show_instructions()

    rand_num = random.randint(1, 100)
    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100: ").strip()

        if user_guess in ['q', 'Exit', 'exit', 'quit']:
            print("Thank you for playing. Goodbye")
            break
        if not validate_input(user_guess=user_guess):
            continue
    
        user_guess = int(user_guess)
        if rand_num > user_guess:
            print("Your guess is too low. Please try again.")

        elif rand_num < user_guess:
            print("Your guess is too high. Please try again")
        else:
            print("Congratulations! You guessed the correct number!")
            print(f" Your score is {score}")

            user_response = input("Would you like to play again?(YES OR NO)")
            if user_response.lower() == 'yes':
                rand_num = random.randint(1, 100)
                score = 100
                continue
            elif user_response.lower() == 'no':
                print('Thank you for playing. Goodbye!')
            else:
                break

        score -= 10
        score = max(0, score)
    
    
if __name__ == '__main__':
    main()