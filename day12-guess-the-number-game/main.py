import random
from logo import logo

DIFFICULTY = {"EASY": 10, "HARD": 5}  # Number of attempts per level


def _clear_screen():
    print("\033[H\033[J")  # Clear screen sequence


def set_difficulty():
    """Returns maximum of attempts based on user input"""
    difficulty = input("Choose a difficulty. Type [e]asy or [h]ard: ")
    if difficulty in ["e", "E"]:
        return DIFFICULTY["EASY"]
    elif difficulty in ["h", "H"]:
        return DIFFICULTY["HARD"]


def check_answer(guess, answer):
    """Checks if user input is equal to the random number"""
    if guess == answer:
        print("Congratulations! You found the right number 🎉")
        return True
    elif guess > answer:
        print("Too high")
    else:
        print("Too low")
    return False


def game_loop(difficulty):
    attempts = 0
    answer = random.randint(1, 100)

    _clear_screen()
    print(logo)
    print("I'm thinking of a number between 1 and 100.")

    while attempts < difficulty:
        print(
            f"You have {difficulty - attempts} attempts remaining to guess the number."
        )
        guess = int(input("Make a guess: "))
        attempts += 1
        if check_answer(guess, answer):
            return

    print(f"You lose 🤕... the number was {answer}")


def main():
    _clear_screen()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    game_loop(set_difficulty())


if __name__ == "__main__":
    main()
