'''
Deck class stores deck of cards, can shuffle it and peek some amount from top
'''
import random

class Deck:
    '''
    Class to represent the Black Jack game
    It contains deck of cards, stored as list of tuples e.g. (2, '♠')
    '''

    def __init__(self):
        '''
        Initializing instance you create a deck of cards
        '''
        self.cards = []

        # For each of possible suites
        for suit in ['♥', '♦', '♣', '♠']:
            # We define numeric values of the cards (except 10)
            for value in range(2, 10):
                self.cards.append((value, suit))
            # Next we define upper values like Ten, Ace, Quinn, etc.
            for value in ['T', 'J', 'Q', 'K', 'A']:
                self.cards.append((value, suit))

    def shuffle(self):
        '''Shuffles cards in the deck'''
        random.shuffle(self.cards)

    def peek(self, amount=1):
        '''
        Method to peek a card from the deck
        INPUT: amount of cards to be returned
        OUTPUT: returns Tuple with the card representation
        '''
        return [self.cards.pop() for i in range(0, amount)]
