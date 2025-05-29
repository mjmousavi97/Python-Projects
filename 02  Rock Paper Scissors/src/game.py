import random 


class RockPaperScissors:
    def __init__(self, name):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices})').strip()
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f'Invalid choice, you must select from ({self.choices}).')
        return self.get_player_choice()

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        
        win_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return "Congratulations! You won"
        
        return 'Oh no. The computer won!'
    
    
    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner_message = self.decide_winner(user_choice, computer_choice)
        print(winner_message)
        print(f"Computer choice: {computer_choice}")


if __name__ == '__main__':
    game = RockPaperScissors('Mohammad Javad')

    while True:
        game.play()

        continue_game = input('Do you want to play again? (Enter any key to play again, enter q to exit)')
        if continue_game.lower() == 'q':
            print('Thank you! See you soon.')
            break