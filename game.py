import random
import helpers
# player vs dealer
player_money = 100
player_life = 3
dealer_life = 3
game_round = 0
is_game_on = True


def draw_card():
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
    i = random.randint(0, len(cards) - 1)
    return cards[i]


def deal_cards():
    return


def print_card(card_hand):
    hand = ''
    for card in card_hand:
        hand += "[" + str(card) + "],"
    return hand


def calculate_score(card_list):
    aces = 0
    score = 0
    for card in card_list:
        if card == 'A':
            aces += 1
        elif card in ['J', 'Q', 'K']:
            score += 10
        else:
            score += card

    if aces:
        for ace in range(aces):
            if score > 11:
                score += 1
            else:
                score += 11
    return score


player_hand = []
card_score = 0
# first deal


# draw 2 cards:
player_hand = []
for i in range(2):
    player_hand.append(draw_card())

# display the card and score on the screen:


while card_score < 22:
    print("Player Hand:")
    card_score = calculate_score(player_hand)
    print(print_card(player_hand), "=", card_score)
    print("Hit/Stick? (h/s)")
    action = input()
