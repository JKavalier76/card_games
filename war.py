#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jkavalier76

Simple War card game

Basic game  details: 
Each player is dealt 26 cards

Each player turns up card at same time -> player with highest card takes 
the others cards

If cards are same rank it's time for War! Each player turns one card face down
and one face up: if turned up cards are again equal, each player places another
card face down and one face up..until one player's face up card beats the other.
Player that wins takes all the cards one the table.

Play continues until one player has won all the cards


Modules needed:
    Deal card(s) to Players (need class for Player?)
    Determine which of two players has highest card
        -> then add losing player's cards to wining player's pile
    War 

"""

import random

suits = "hearts spades clubs diamonds".split()

rankings = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

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
        str = self.ranking + " of " + self.suit
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


def initial_deal(deck, player1, player2):
    # Deals all 52 cards to two players. Player 1 assumed to be the dealer

    for i in range(len(deck)):
        pass



# BELOW IS TEMP CODE TO CHECK FUNCTIONALITY WORKS  

deck = Deck()
# print(len(deck))
for i in deck:
    print(SUIT_SYMBOLS[i.suit] + i.ranking)
    
x = deck.deal(3)
# print(x)
# print(len(deck))
