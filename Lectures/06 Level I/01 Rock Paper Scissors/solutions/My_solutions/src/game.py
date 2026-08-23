import random


class RockPaperScissors:
    """Main class for Rock Paper Scissors game."""
    def __init__(self, name: str):
        self.choice = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        user_choice: str = input(f'Enter your choice ({self.choice}): ')
        if user_choice.lower() in self.choice:
            return user_choice.lower()
        else:
            print(f'Invalid choice, you must select from {self.choice}.')
            return self.get_player_choice()

    def get_computer_choice(self):
        """Get computer choice randomly from choices: rock, paper, scissors."""
        return random.choice(self.choice)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decide the winner of the game based on user and computer choices.

        :param user_choice: The choice of the user.
        :param computer_choice: The choice of the computer.
        :return: The result of the game. (who won!)
        """
        if user_choice == computer_choice:
            return 'It is a Tie!'

        win_combinations = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return "congratulations you won"

        return "oh no! the computer won"

    def play(self):
        """Play the game.
        - Get user choice.
        - Get computer choice.
        - Decide the winner.
        - Print the result.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"computer choice: {computer_choice}")
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == '__main__':
    game = RockPaperScissors('Mohsen')

while True:
    game.play()

    continue_game = input('Do you want to play again? (Enter any key to play again, enter q to exit!)')
    if continue_game.lower() == 'q':
        break