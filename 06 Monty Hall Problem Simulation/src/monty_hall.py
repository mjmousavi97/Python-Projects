import random


def monty_hall_game(switch_doors):
    """
    Simulate one round of the Monty Hall game.

    In the Monty Hall problem, there are three doors: behind one is a car (the prize), and behind the other two are goats.
    The player chooses one door. The host, who knows what is behind the doors, opens another door that has a goat.
    The player can then choose to switch their choice to the remaining unopened door.

    :param switch_doors: Boolean indicating whether the player switches their choice after one goat door is revealed.
    :type switch_doors: bool
    :return: True if the player wins the car, False otherwise.
    :rtype: bool
    """
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    if switch_doors:
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        door_revealed = random.choice(doors_revealed)

        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'


def simulate_game(num_game):
    """
    Run multiple simulations of the Monty Hall game and compute win probabilities with and without switching.

    :param num_game: Number of times to simulate the Monty Hall game.
    :type num_game: int
    :return: A tuple containing:
             - win rate when switching doors (float)
             - win rate when not switching doors (float)
    :rtype: tuple
    """
    num_wins_without_switching = 0
    for _ in range(num_game):
        if monty_hall_game(False):
            num_wins_without_switching += 1

    num_wins_by_switching = num_game - num_wins_without_switching

    return num_wins_by_switching, num_wins_without_switching


if __name__ == '__main__':
    num_games = 10000
    num_wins_by_switching, num_wins_without_switching = simulate_game(num_games)
    print(f"Number of wins with switching is: {num_wins_by_switching}")
    print(f"Number of wins without switching is: {num_wins_without_switching}")
