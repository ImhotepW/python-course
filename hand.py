'''
Hand class handles player's cards in the hand, can hit, print all cards in a hand and calculate score
'''
class Hand:
    '''
    Class to represent player's hand
    '''

    def __init__(self, name, cards=[]):
        '''
        To initialise player's hand you need to provide a list with tuples
        For instance [(2, '♠'), ([)'A', '♥')]
        '''
        self.name = name
        self.cards = cards
        self.score = self.get_score()


    def print_hand(self, hide_last=False):
        '''
        Draws a hand in a readable form
        INPUTS: if hide_last is True last card of the Hand will be printed face down
        OUTPUT: string representing cards in the Hand
        '''
        print('{} hand:'.format(self.name))
        cards_cnt = len(self.cards)
        prnt = ' _____    '*len(self.cards)+'\n'
        prnt += '|     |   '*len(self.cards)+'\n'
        for i in range(0, cards_cnt):
            prnt += '|  {}  |   '.format('*' if (hide_last and i == cards_cnt-1) else self.cards[i][0])
        prnt += '\n'
        prnt += '|     |   '*len(self.cards)+'\n'
        for i in range(0, cards_cnt):
            prnt += '|  {}  |   '.format('*' if (hide_last and i == cards_cnt-1) else self.cards[i][1])
        prnt += '\n'
        prnt += '|_____|   '*len(self.cards)+'\n'

        return prnt

    def hit(self, card):
        '''Peek card to the Hand'''
        self.cards += card
        self.score = self.get_score()

    def get_score(self):
        '''Returns overall score of the player's hand'''
        score = 0
        for card in self.cards:
            if card[0] in ['T', 'J', 'Q', 'K']:
                score += 10
            elif card[0] == 'A':
                if score + 11 <= 21:
                    score += 11
                else:
                    score += 1
            else:
                score += card[0]
        return score


    def __str__(self):
        '''String representation of the Hand class'''
        return self.print_hand()
