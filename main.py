import random
import lib
# Python blackjack main file


# Welcome text:
print("BLACKJACK!")

# draw a card:
# draws a random card out of the deck


player_hand = []
player_card_count = 0

# draw two cards for the player
for i in range(2):
    player_hand.append(lib.draw_card())

# calculate the player score
# player_card_count = lib.calculate_score(player_hand)
action = 'h'
# first loop to keep dealing for the player
while player_card_count < 21 and action == 'h':
    print("Your hand:")
    player_card_count = lib.calculate_score(player_hand)
    print(lib.print_card(player_hand), "=", player_card_count)
    print("Do you want to hit/stick?")
    action = input()
    # if the player hits, draw a new card:
    if action == 'h':
        player_hand.append(lib.draw_card())

if player_card_count == 21:
    print("BLACKJACK")

if player_card_count > 21:
    print("BUSTED!")
    print("Dealer wins.")
