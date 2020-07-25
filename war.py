#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jkavalier76

Simple "War" card game

Game ends when all cards from initial deal have been dealt - does not continue
until one "player" has won all cards like some versions of the game. 

If last hand is "war" (and neither "player" has enough cards to play war) then
the hand is considered a tie. 

"""

import random

suits = "hearts spades clubs diamonds".split()

rankings = "2 3 4 5 6 7 8 9 10 J Q K A".split()

SUIT_SYMBOLS = {
    'spades': u'♠',
    'diamonds': u'♦',
    'clubs': u'♣',
    'hearts': u'♥',
}


class Card:

    def __init__(self, suit, ranking):
        self.suit = suit
        self.ranking = ranking

    def __repr__(self):
        str = SUIT_SYMBOLS[self.suit] + self.ranking
        return(str)


class Deck:

    def __init__(self):
        self.deck = []
        for i in suits:
            for j in rankings:
                self.deck.append(Card(i, j))
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return iter(self.deck)

    def __getitem__(self, position):
        return self.deck[position]

    def deal(self, num_cards):
        """
        Deals num_cards number of cards and removes them from the deck and
        returns a list
        """
        return [self.deck.pop() for i in range(num_cards)]


class Player:

    def __init__(self):
        self.hand = []

    def __len__(self):
        return len(self.hand)

    def __iter__(self):
        return iter(self.hand)

    def __getitem__(self, position):
        return self.hand[position]

    def flip_card(self, num_cards):
        return [self.hand.pop() for i in range(num_cards)]


def initial_deal(deck, player1, player2):

    '''
    Deals all 52 cards to two players. Player 1 assumed to be the dealer.
    First, player 2 gets every other card in the shuffled deck. Player 1 gets
    remaining cards.
    '''

    for i in range(0, len(deck), 2):
        player2.hand += deck.deal(1)

    player1.hand += deck.deck  # Give player 1 (delear) all remaining cards


def get_ranking(card):
    '''
    returns index of a card ranking from list "rankings" as a way to compare
    two cards and determine which one wins
    '''

    return rankings.index(card.ranking)


def determine_winner(player_1_card, player_2_card):
    return [player_1_card, player_2_card]


def war(player1, player2, p1_pile, p2_pile):
    tie = True
    while tie and (len(player_1.hand) > 2) and (len(player_2.hand) > 2):
        p1_pile += player1.flip_card(2)
        p2_pile += player2.flip_card(2)
        print("Player 1 draws: X and {}".format(p1_pile[-1]))
        print("Player 2 draws: X and {}\n".format(p2_pile[-1]))

        if get_ranking(p1_pile[-1]) > get_ranking(p2_pile[-1]):
            print("Player 1 wins! \n")
            p1_pile += p2_pile
            tie = False
            return(1, p1_pile)
        elif get_ranking(p1_pile[-1]) < get_ranking(p2_pile[-1]):
            print("Player 2 wins! \n")
            p2_pile += p1_pile
            tie = False
            return(2, p2_pile)
        else:
            print("!!War Again!!")


#  BELOW IS MAIN PLAY CODE

deck = Deck()
player_1 = Player()
player_2 = Player()
initial_deal(deck, player_1, player_2)
p1_discard_pile = []  # These are the piles of cards already played
p2_discard_pile = []

round = 0  # will count how many rounds it takes to finish game
while (len(player_1.hand) > 0) and (len(player_2.hand) > 0):
    p1_current_pile = []  # Current hand pile. Usually 1 card unless in war.
    p2_current_pile = []
    round += 1
    print("************ Round {} ************\n".format(round))

    p1_total_cards = len(player_1.hand) + len(p1_discard_pile)
    p2_total_cards = len(player_2.hand) + len(p2_discard_pile)

    print("Player 1 has {} total cards: {} holding and {} discarded"
          .format(p1_total_cards, len(player_1.hand), len(p1_discard_pile)))
    print("Player 2 has {} total cards: {} holding and {} discarded\n"
          .format(p2_total_cards, len(player_2.hand), len(p2_discard_pile)))

    p1_current_pile += player_1.flip_card(1)
    p2_current_pile += player_2.flip_card(1)

    print("Player 1 draws: {}".format(p1_current_pile[0]))
    print("Player 2 draws: {}\n".format(p2_current_pile[0]))

    if get_ranking(p1_current_pile[0]) > get_ranking(p2_current_pile[0]):
        print("Player 1 wins round {}! \n".format(round))
        p1_discard_pile += p1_current_pile + p2_current_pile
    elif get_ranking(p1_current_pile[0]) < get_ranking(p2_current_pile[0]):
        print("Player 2 wins round {}! \n".format(round))
        p2_discard_pile += p1_current_pile + p2_current_pile
    else:
        if (len(player_1.hand) > 2) and (len(player_2.hand) > 2):
            print("!!War!!\n")
            winner, war_pile = war(player_1, player_2, p1_current_pile,
                                   p2_current_pile)
            if winner == 1:
                p1_discard_pile += war_pile
            else:
                p2_discard_pile += war_pile

p1_total_cards = len(player_1.hand) + len(p1_discard_pile)
p2_total_cards = len(player_2.hand) + len(p2_discard_pile)
print("Final score: {} cards for Player 1, {} cards for Player 2"
      .format(p1_total_cards, p2_total_cards))