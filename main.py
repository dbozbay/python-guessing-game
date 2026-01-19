import random


def print_welcome_msg(min_num: int, max_num: int) -> None:
    title = "GUESSING GAME"
    border = "=" * 40

    print(
        f"{border}\n"
        f"{title:^40}\n"
        f"{border}\n\n"
        f"I'm thinking of a number between {min_num} and {max_num}...\n"
        f"Guess the number!\n"
    )


def print_winner_msg(attempts: int) -> None:
    border = "-" * 40
    attempt_word = "attempt" if attempts == 1 else "attempts"

    print(
        f"\n{border}\nCongratulations, you won! ({attempts} {attempt_word})\n{border}"
    )


def get_user_guess(min_num: int, max_num: int) -> int:
    while True:
        try:
            guess = int(input("Enter your guess: "))

            if min_num <= guess <= max_num:
                return guess
            else:
                print(
                    f"Error: Please enter a number between {min_num} and {max_num}.\n"
                )

        except ValueError:
            print("Error: That is not a valid number. Please try again.\n")


def guessing_game(min_num: int = 1, max_num: int = 100) -> None:
    print_welcome_msg(min_num, max_num)

    secret_number = random.randint(min_num, max_num)
    guessed_numbers = set()

    while True:
        guess = get_user_guess(min_num, max_num)
        guessed_numbers.add(guess)

        if guess > secret_number:
            print("Too big! Try again...\n")
        elif guess < secret_number:
            print("Too small! Try again...\n")
        else:
            print_winner_msg(len(guessed_numbers))
            break


if __name__ == "__main__":
    guessing_game(1, 10)
