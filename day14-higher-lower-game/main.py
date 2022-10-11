import random
from logo import logo, vs
from game_data import data


def check_answer(ans, acct_a, acct_b):
    """Returns `True` if the player chose the right answer"""
    if has_more_follow(acct_a, acct_b):
        return ans == 'a'
    else:
        return ans == 'b'


def has_more_follow(acct_a, acct_b):
    """Returns `True` if Account A has more followers than Account B"""
    return acct_a['follower_count'] > acct_b['follower_count']


def clear_screen():
    print('\033[H\033[J')  # Clear screen sequence


def main():
    score = 0
    is_game_over = False

    account_b = random.choice(data)

    print(logo)

    while not is_game_over:

        account_a = account_b
        while account_b == account_a:
            account_b = random.choice(data)

        print(
            f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}"
        )
        print(vs)
        print(
            f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}"
        )

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        clear_screen()
        print(logo)

        if check_answer(answer, account_a, account_b):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")


if __name__ == '__main__':
    main()
