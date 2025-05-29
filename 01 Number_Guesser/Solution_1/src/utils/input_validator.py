def get_valid_input(start: int, end: int) -> int:
    """
    Repeatedly prompts the user to enter an integer between 'start' and 'end' (inclusive).

    :Parameters:
    start (int): The minimum acceptable value (inclusive).
    end (int): The maximum acceptable value (inclusive).

    :Returns:
    int: A valid integer entered by the user within the specified range.

    The function keeps asking until a valid integer is entered.
    It handles non-integer input and out-of-range values with appropriate messages.
    """
    while True:
        try:
            user_input = int(input('Enter a number: '))
            if start <= user_input <= end:
                return user_input
            else:
                print(f'Invalid input. Please enter a number between {start} and {end}')
                continue
        except ValueError:
            print(f'Invalid input. Please enter a number between {start} and {end}.')
            continue

if __name__ == '__main__':
    print(get_valid_input(1, 100))