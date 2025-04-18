import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

rank = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
          "Jack", "Queen", "King", "Ace")

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,
        "Jack":10, "Queen":10, "King":10, "Ace":11}

class Card:
    '''
    Gives a card all of its characteristics.
    '''

    def __init__(self, suits, rank, values):

        self.suits = suits
        self.rank = rank
        self.values = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suits

class Deck:

    def __init__(self):
        
        self.all_cards = []


    def __str__(self):
        pass

    def shuffle(self):
        pass

    def deal(self):
        pass

class Hand:

    def __init__(self):
        pass

    def add_card(self):
        pass
    
    def adjust_for_ace(self):
        pass

class Chips:

    def __init__(self):
        pass

    def win_bet(self):
        pass

    def lose_bet(self):
        pass