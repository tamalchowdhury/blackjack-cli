import random


def draw_card():
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
    i = random.randint(0, len(cards) - 1)
    return cards[i]


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
