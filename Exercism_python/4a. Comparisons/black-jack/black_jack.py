"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


# Additional concepts about NaN. NaN == NaN is false. It is part of floating-point operations. Therefore, use float('NaN') to create NaN
# float type understands concept of NaN, otherwise it is treated as a regular string

# use math module's function math.isnan() to check if something is Not a Number

# use ord() to return a character or string's Unicode character.
# Comparison Chaining can be done in python e.g.: x < y <= z

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card == 'A':
        return 1
    elif card in ('K','J','Q'):
        return 10
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)

    if card_one_val > card_two_val:
        return card_one
    elif card_one_val < card_two_val:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if 'A' not in (card_one, card_two):
        hand = sum((value_of_card(card_one), value_of_card(card_two)))

    if card_one == 'A' or card_two == 'A' or hand >= 11:
        return 1
    else:
        return 11

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    hand_value = 0

    for card in (card_one, card_two):
        if card == 'A':
            if hand_value <=10:
                hand_value += 11
            else:
                hand_value += 1
        else:
            hand_value += value_of_card(card)
        print(hand_value)

    return True if hand_value == 21 else False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return (value_of_card(card_one) == value_of_card(card_two))

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    return (9 <= int(sum( (value_of_card(card_one), value_of_card(card_two)) )) <= 11)

print(can_double_down('A', '9'))
print(can_double_down('10', '2'))
# print('성격' > '아름다운')
# print('ব্যক্তিত্ব' > 'সুন্দর')
# print('व्यक्तित्व' > 'सुंदर')
# print('شخصیت' > 'خوبصورت')
# print('personality' > 'beautiful')