def provide_hint(guess: int, actual_number: int) -> None:
    """
    Provides a hint to the user based on their guess compared to the actual number.

    :Parameters:
    guess (int): The number guessed by the user.
    actual_number (int): The correct number to be guessed.

    :Returns:
    None: This function does not return anything. It prints a hint message instead.

    The function compares the guess to the actual number and prints whether the guess is too low or too high.
    """
    if guess < actual_number:
        print('Your guess is too low')
    elif guess > actual_number:
        print('Your guess is too high')