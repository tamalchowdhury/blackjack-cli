import random
# Python blackjack main file


# Welcome text:
print("BLACKJACK!")

# deck of cards:
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']

# draw a card:
# draws a random card out of the deck


def draw_card():
    i = random.randint(0, len(cards) - 1)
    return cards[i]


action = 'h'
current_hand = ''

while action == 'h':
    card = draw_card()
    current_hand += "[" + str(card) + "],"
    print(current_hand)
    print("HIT/STICK?")
    action = input()
