"""exercise 02 - Wordle"""

__author__: str = "730774516"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # initializing variables to keep track of throughout the game
    turn_count: int = 1
    game_won: bool = False
    # the while loop that the game takes place in
    # it asks for guesses, counts turns, and returns the emojified str
    while game_won is False and turn_count <= 6:
        print(f"=== Turn {turn_count}/6 ===")
        turn_count += 1
        guess = input_guess(len(secret))
        guess_emoji = emojified(guess, secret)
        print(guess_emoji)
        if guess == secret:
            game_won = True
            print(f"You won in {turn_count - 1}/6 turns!")
    if turn_count > 6 and game_won is False:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, letter: str) -> bool:
    """returns True or False after checking if letter is in word"""
    assert len(letter) == 1, f"len('{letter}') is not 1"
    count_contains: int = 0
    n: int = 0
    # i am using this n to increase the index for each iteration
    while count_contains == 0 and n < (len(word)):
        if word[0 + n] == letter:
            count_contains += 1
            n += 1
        else:
            n += 1
    if count_contains == 0:
        return False
    else:
        return True


def emojified(guess: str, secret: str) -> str:
    """returns a str of emojis with color corresponding to guess accuracy"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    # emoji codes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_str: str = ""
    # i didn't create a separate variable for indexing
    # because i figured the len of this string was equivalent
    while len(emoji_str) < (len(secret)):
        if guess[0 + len(emoji_str)] == secret[0 + len(emoji_str)]:
            emoji_str += GREEN_BOX
        elif contains_char(secret, guess[0 + len(emoji_str)]) is True:
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
    return emoji_str


def input_guess(exp_len: int) -> str:
    """prompts for guess of exp_len length and returns guess"""
    guess_input: str = input(f"Enter a {exp_len} character word:")
    # not used for indexing or iteration
    # i just needed a way for the while loop to run even if the len is correct
    while len(guess_input) != exp_len:
        guess_input = input(f"That wasn't {exp_len} chars! Try again:")
    return guess_input


if __name__ == "__main__":
    main(secret="codes")
