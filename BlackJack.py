import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
          "Jack", "Queen", "King", "Ace")

values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,
        "Jack":10, "Queen":10, "King":10, "Ace":11}

playing = True

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
        Adds a card to the player's hand, then gets the sum of cards in hand.
        '''
        
        self.cards.append(card)

        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1


    def adjust_for_ace(self):
        '''
        Adjusts value of aces depending on total value of cards in hand.
        '''
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):

        return f"{self.value}"

class Chips:

    '''
    Keeps track of a player's total chips.
    '''

    def __init__(self):
        
        self.total = 100
        self.bet = 0

    def win_bet(self):
        '''
        Adds chips to player's total if they win.
        '''

        self.total += self.bet

    def lose_bet(self):
        '''
        Removes chips from player's total if they lose.
        '''

        self.total -= self.bet

def take_bet(chips):
    '''
    Asks a player to enter a whole number less than or equal to their total.
    '''

    while True:
        try:
            chips.bet = int(input("How much do you want to bet? : "))
    
        except ValueError:
            print("Must enter a whole number. ")

        else:
            if chips.bet > chips.total:
                print(f"Your bet can't exceed your total: {chips.total}")

            else:
                break

def hit(deck,hand):
    '''
    Deals a card and then checks if it's an ace.
    '''

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    '''
    Asks the player if they would like to hit or stand.
    '''

    global playing

    while True:

        is_hit = input("Would you like to hit or stand? (hit / stand): ")
        if is_hit.lower() == "hit":
            hit(deck,hand)
        elif is_hit.lower() == "stand":
            print("Player stands.")
            playing = False
        else:
            print("Please try again.")
            continue
        break

def show_some(player,dealer):
    '''
    Shows the player's cards and hides the dealer's first card.
    '''

    print("Player's hand: ",*player.cards)
    print(f"Dealer's hand: {dealer.cards[1]}")

def show_all(player,dealer):
    '''
    Shows all cards in player's and dealer's hand.
    '''

    print("Player's hand: ", *player.cards, f"Value: {player.value}")
    print("Dealer's hand: ", *dealer.cards, f"Value: {dealer.value}")

def player_busts(player,dealer,chips):
    '''
    If the player goes over 21.
    '''

    print("Player busts!")

    chips.lose_bet()


def player_wins(player,dealer,chips):
    '''
    If the player beats the dealer.
    '''

    print("Player wins!")

    chips.win_bet()

def dealer_wins(player,dealer,chips):
    '''
    If the dealer beats the player.
    '''

    print("Dealer wins!")

    chips.lose_bet()

def dealer_busts(player,dealer,chips):
    '''
    If the dealer goes over 21.
    '''

    print("Dealer busts!")

    chips.win_bet()

def push(player,dealer):
    '''
    If a tie happens.
    '''

    print("Dealer and Player tie! it's a push.")

player_chips = Chips()

while True:
#Sets up the game creating and shuffling deck, ask how many chips the player has total, 
#asks how much they would like to bet, deals 2 cards to player and dealer,
#and shows cards except the dealer's first card.

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal())
            
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
            
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)       

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

    print(f"You have {player_chips.total} chips. ")

    again = input("Would you like to play again? (y / n)")
    
    if again.lower() == "y":
        playing = True
        continue
    else:
        break
    