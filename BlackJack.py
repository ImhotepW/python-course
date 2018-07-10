from IPython.display import clear_output
from Deck import Deck
from Hand import Hand

def request_bet(balance):
    '''This function requests the player to bet some amount of the balance '''
    the_bet = 0
    while the_bet == 0: 
        try:
            the_bet = int(input('Place your bet: '))
            if the_bet > balance:
                the_bet = 0
                print('Not enough balance!')
        except ValueError:
            print('Please, input ingeger value!')
    return the_bet    

def questing(message ,variants):
    '''Ask player something in message
    OUTPUT: return True if player choose first two of provided variants, otherwise False
    '''
    answer = ''
    while answer not in variants:
        answer = input(message).lower()
    return answer in variants[0:1]


print('Welcome to Black Jack!')

# Assigning balance
balance = 100
bet = 0

while True:
    deck = Deck()
    deck.shuffle()
    player = Hand('Player', deck.peek(2))
    dealer = Hand('Dealer', deck.peek(2))
    # Initial deck
    print("Your balance is {}".format(balance))
    bet = request_bet(100)
    print("Cool, let's start! Drawing cards...\n")
    print(dealer.print_hand(True))
    print(player)
    
    # Player turn
    while player.score < 21 and questing('How do you like it? Whant to (H)it or (S)tand? ', ['h','hit','s','stand']):
        player.hit(deck.peek())        
        #print('\n'*100)
        clear_output()
        print("Your balance is {}".format(balance))
        print(dealer.print_hand(True))
        print(player)
        if player.score > 21:
            break
    
    # Dealer turn
    while dealer.score <= 21 and player.score < 21:
        dealer.hit(deck.peek())
    
    # Final deck
    clear_output()
    #print('\n'*100)
    print("Your balance is {}".format(balance))
    print(dealer)
    print(player)
    
    # And the winner is
    if player.score > 21:
        print('Bust! Sorry, but you loose your bet...')
        balance -= bet
    elif dealer.score > 21:
        print('Bust! Dealer loose... You WIN {}!!!'.format(bet))
        balance += bet
    elif (dealer.score == player.score):
        print('Push! Your bet is back...')
        balance += bet
    elif dealer.score > player.score :
        print('Dealer WIN! Sorry, but you loose your bet...')
    elif dealer.score < player.score :
        print('Congratulations, you WIN {}!!!'.format(bet))
        balance += bet
    else:
        pass

    if balance == 0 or questing('Would you like to (L)eave or (S)tay and contunue? ',['l','leave','s','stay']):
        print('Thank you for playing with us!')
        print('Your final balance is {}'.format(balance))
        print('Good Bye!')
        break
    else:
        #print('\n'*100) 
        clear_output()