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
            if score >= 11:
                score += 1
            else:
                score += 11
    return score
