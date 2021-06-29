# Copyright 2021 Tamal Anwar Chowdhury

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Python blackjack main file

import random
import lib
import table
import time

player_money = 100
round_number = 1
playing = True

while player_money and playing:
    # draw a card:
    # draws a random card out of the deck
    player_hand = []
    dealer_hand = []
    player_card_count = 0
    dealer_card_count = 0
    is_player_standing = True
    is_dealer_standing = True
    result = ''
    # draw two cards for the player and dealer
    for i in range(2):
        player_hand.append(lib.draw_card())
        dealer_hand.append(lib.draw_card())

    # calculate the player score
    player_card_count = lib.calculate_score(player_hand)
    dealer_card_count = lib.calculate_score(dealer_hand)
    action = 'h'

    # first loop to keep dealing for the player
    while player_card_count < 21 and action == 'h':
        table.draw_table(dealer_hand, player_hand, True)
        print("BLACK-JACK!!")
        print("Round:", round_number)
        print("Card total =", player_card_count)
        print("Do you want to [h]it/[s]tick?")
        action = str.lower(input())
        # if the player hits, draw a new card:
        if action == 'h':
            player_hand.append(lib.draw_card())
            player_card_count = lib.calculate_score(player_hand)

    if player_card_count == 21:
        result = "YOU WIN!"
        player_money += 20
        is_dealer_standing = False

    if player_card_count > 21:
        result = "HOUSE WINS!"
        player_money -= 20
        is_player_standing = False

    # player is still standing, deal the dealer:
    while is_player_standing and is_dealer_standing:
        # print the dealer and player cards:
        print("Dealer is dealing...")
        time.sleep(2)
        table.draw_table(dealer_hand, player_hand, False)
        print("Your card total =", player_card_count)
        print("Dealer card total =", dealer_card_count)
        if is_player_standing:
            dealer_hand.append(lib.draw_card())
            dealer_card_count = lib.calculate_score(dealer_hand)

        if dealer_card_count > player_card_count:
            is_player_standing = False
            player_money -= 20
            result = "HOUSE WINS!"

        if dealer_card_count > 21:
            is_dealer_standing = False
            player_money += 20
            result = "YOU WIN!"

    # Print the table at the end:
    table.draw_table(dealer_hand, player_hand, False)
    print("Your card total =", player_card_count)
    print("Dealer card total =", dealer_card_count)
    print(result, "Total money:", player_money)
    cont = input("<<< CONTINUE? >>> y/n\n")
    if str.lower(cont) == 'n':
        playing = False
    round_number += 1
