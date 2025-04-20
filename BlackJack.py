import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
          "Jack", "Queen", "King", "Ace")

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,
        "Jack":10, "Queen":10, "King":10, "Ace":11}

class Card:
    '''
    Gives a card all of its characteristics.
    '''

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit} {self.value}"

class Deck:

    '''
    Creates a deck, shuffles deack, then deals cards.
    '''

    def __init__(self):
        
        #Create empty deck.
        self.deck = []

        #Create and add card objects to deck.
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def shuffle(self):
        '''
        Shuffles the deck.
        '''
        
        random.shuffle(self.deck)

    def deal(self):
        '''
        Deals a card.
        '''
        
        return self.deck.pop(0)

class Hand:
    '''
    Shows which cards are in a player's hand, the value they add up to, and if they have any aces.
    '''

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        '''
        Adds a card to the player's hand.
        '''
        
        self.cards.append(card)

    def adjust_for_ace(self):
        '''
        Adjusts value of aces depending on total value of cards in hand.
        '''
        
        pass

    def __str__(self):

        return f"{self.cards[0].value}"

class Chips:

    def __init__(self):
        pass

    def win_bet(self):
        pass

    def lose_bet(self):
        pass

testhand = Hand()
testdeck = Deck()
testdeck.shuffle()

testhand.add_card(testdeck.deal())
testhand.add_card(testdeck.deal())
testhand.value

print(testhand)
