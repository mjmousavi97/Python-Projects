import random 


class RockPaperScissors:
    """
    A simple Rock-Paper-Scissors game between a player and the computer.
    The class handles user input, computer's random choice, and decides the winner.
    """

    def __init__(self, name: str):
        """
        Initialize the game with the player's name.

        :param name: The player's name.
        :type name: str
        """
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self) -> str:
        """
        Ask the player to enter a choice and validate the input.
        Keeps asking until a valid choice is entered.

        :return: The validated player choice.
        :rtype: str
        """
        while True:
            user_choice = input(f'Enter your choice ({self.choices}): ').strip().lower()
            if user_choice in self.choices:
                return user_choice
            print(f'Invalid choice, pick one of {self.choices}.')

    def get_computer_choice(self) -> str:
        """
        Randomly generate the computer's choice.

        :return: The computer's randomly chosen option.
        :rtype: str
        """
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """
        Compare the player and computer choices and decide who wins.

        :param user_choice: The player's choice.
        :type user_choice: str
        :param computer_choice: The computer's choice.
        :type computer_choice: str
        :return: Message with the result of the round.
        :rtype: str
        """
        if user_choice == computer_choice:
            return "It's a Tie!"
        
        # Winning pairs (player beats computer)
        win_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        if (user_choice, computer_choice) in win_combinations:
            return f"Congratulations {self.player_name}, you won!"
        
        return "The computer won this round."

    def play(self) -> None:
        """
        Play a single round of the game:
        - Get player input
        - Generate computer choice
        - Show the result

        :return: None
        :rtype: None
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"{self.player_name}'s choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':
    """
    Entry point of the game. 
    Runs in a loop until the player decides to quit.
    """
    user_name = input('Enter your name, please: ').strip()
    game = RockPaperScissors(user_name)

    while True:
        game.play()
        continue_game = input('Play again? (q to quit): ')
        if continue_game.lower() == 'q' or continue_game.lower() == 'quit':
            print(f'Thank you {user_name}! See you soon')
            break
