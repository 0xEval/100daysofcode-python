############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from time import sleep
from logo import logo

################# Constants ####################

BLACKJACK = 21
MINIMUM_SCORE = 17

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

##################### Game Logic #####################


class Player:
    def __init__(self):
        self.hand = []
        self.is_playing = True
        self.hand_score = 0


def get_random_card():
    """Returns a random card from `cards`"""
    return random.choice(cards)


def deal_card(player):
    """Appends a random card to `player`'s deck"""
    player.hand.append(get_random_card())


def calculate_score(player):
    """Calculates the sum of the value of all cards in a player's hand.
    Replaces Ace (11) for One (1) if the total if above 21 (bust)."""
    if sum(player) > 21:
        player[:] = [1 if card == 11 else card for card in player]
    return sum(player)


def compare(player, dealer):
    """Returns string determining who won the game"""

    if player.hand_score > BLACKJACK:
        return "You went bust 🤪. You lose."

    # Dealer always wins if its total score is 21
    if dealer.hand_score == BLACKJACK:
        return "Dealer wins with a Blackjack 😱"

    if dealer.hand_score == player.hand_score:
        return "Its a draw 😃"

    if player.hand_score == BLACKJACK:
        return "You win with a Blackjack 😎"

    if dealer.hand_score > BLACKJACK:
        return "Dealer went bust. You win 💪"

    if player.hand_score > dealer.hand_score:
        return "Your score is greater. You win 🥳"
    else:
        return "Your score is weaker. You lose 🤕"


def game_loop():
    player, dealer = Player(), Player()

    deal_card(player)  # Deal card to Player
    deal_card(player)
    deal_card(dealer)

    player.hand_score = calculate_score(player.hand)
    dealer.hand_score = calculate_score(dealer.hand)

    while player.is_playing:

        print("\033[H\033[J")  # Clear screen sequence
        print(logo)
        print(f"Your Hand: {player.hand} - Total {player.hand_score}")
        print(f"Dealer's First Card: {dealer.hand[0]}")

        if player.hand_score < BLACKJACK:

            next_move = input("Would you like another card? type [y]es or [n]o. ")

            if next_move in ["Y", "y", ""]:
                deal_card(player)  # Player Hits
                player.hand_score = calculate_score(player.hand)

        player.is_playing = False

    while dealer.is_playing:

        print("\033[H\033[J")  # Clear screen sequence
        print(logo)
        print(f"Your Hand: {player.hand} - Total {player.hand_score}")
        print(f"Dealer's Hand: {dealer.hand} - Total {dealer.hand_score}")

        if dealer.hand_score < MINIMUM_SCORE:
            deal_card(dealer)
            dealer.hand_score = calculate_score(dealer.hand)
            sleep(0.75)  # Add insane game tension
        else:
            dealer.is_playing = False

    result = compare(player, dealer)
    print(result)


def main():
    print(logo)
    while input("Would you like to play a game? type [y]es or [n]o. ") in [
        "Y",
        "y",
        "",
    ]:
        game_loop()


if __name__ == "__main__":
    main()
