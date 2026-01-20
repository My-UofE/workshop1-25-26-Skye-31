import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    n = len(poss_values)
    x = poss_values[n // 2]
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val: int, next_val: int, user_input: str):
    lower = user_input.lower()
    if lower == 'h':
        return next_val > current_val
    elif lower == 'l':
        return next_val < current_val
    else:
        return False


# function to be used in game_3: Hangman
def process_guess(letter: str, board: list[str], word: str):
    letter = letter.lower()
    if letter in word:
        for i, char in enumerate(word):
            if letter == char:
                board[i] = letter
        print("Well done! '" + letter + "' is in the word")
        return True

    else:
        print("Sorry, '" + letter + "' is not in the word")
        return False

    pass
