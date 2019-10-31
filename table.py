# print("===============================")
# print("||---------BLACKJACK---------||")
# print("||          [K][░]           ||")
# print("||                           ||")
# print("||                           ||")
# print("||                           ||")
# print("||        [A][K][5]          ||")
# print("||       total = 16          ||")
# print("===============================")

# print("===============================")
# print("||---------BLACKJACK---------||")
# print("||          [K][░]           ||")
# print("||                           ||")
# print("||                           ||")
# print("||                           ||")
# print("||        [A][K][5]          ||")
# print("||       total = 16          ||")
# print("===============================")

WIDTH = 30


def draw_line(cards=[]):
    line = ""
    line += "||"
    half_space = (WIDTH-4)//2
    if cards:
        # calculate the card width and the space width
        half_space = (WIDTH-4-(3*len(cards)))//2
    # draw the left half of the spaces
    for i in range(half_space):
        line += " "
    if cards:
        for card in cards:
            line += "[" + str(card) + "]"
        # for the extra spacing for fit
        if not len(cards) % 2 == 0:
            line += " "
    for i in range(half_space):
        line += " "
    line += "||"
    print(line)


def draw_table(dealer_cards, player_cards, is_dealer_hidden):
    # draw the top border:
    border = ""
    for i in range(WIDTH):
        border += "="
    print(" ")  # blank line
    print(border)
    draw_line()
    draw_line(dealer_cards)
    draw_line()
    draw_line()
    draw_line()
    draw_line(player_cards)
    draw_line()
    print(border)
