import DeckMaker
import PlayerMaker

deck = DeckMaker.create_shuffeled_deck()
player = PlayerMaker.make_player()

bet = 10
player_hand = []
dealer_hand = []

def place_bet():
    print('current chips:' + str(player.chips))

    while True:
        bet = int(input('place your bet.'))
        if bet > player.chips:
            print('not enough chips')
        else:
            player.chips -= bet
            break
    
    return bet

def deal_cards():
    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))

    player_hand.append(deck.pop(0))
    dealer_hand.append(deck.pop(0))

    show_player_hand()
    print('dealer hand:')
    print(dealer_hand[0])
    print('XXXXXXXXXXXX')
    print(dealer_hand[0].value)

def dealer_takes_card():
    dealer_hand.append(deck.pop(0))

def player_takes_card():
    player_hand.append(deck.pop(0))

def show_player_hand():
    print('player hand:')
    for card in player_hand:
        print(card)
    print(get_player_hand_value())

def show_dealer_hand():
    print('Dealer hand:')
    for card in dealer_hand:
        print(card)
    print(get_dealer_hand_value())

def get_player_hand_value():
    player_hand_value = 0
    for card in player_hand:
        player_hand_value += card.value
    # if player_hand_value > 21 and card.value == 11 in player_hand:
    #     pass
    return player_hand_value

def get_dealer_hand_value():
    
    dealer_hand_value = 0
    for card in dealer_hand:
        dealer_hand_value += card.value
    return dealer_hand_value

    


class Hand():

    def __init__(self, cards):
        self.cards = []
        self._value = 0

    def __str__(self):
        return 'name: ' + self.name + ' chips: ' + str(self.chips)
    
    @property
    def value(self):
        return self._value

    @value.setter
    def set_value(self):
        if card.rank == 'Ace' in self.cards:
        # for card in player_hand:
        #     player_hand_value += card.value
    # if player_hand_value > 21 and card.value == 11 in player_hand:
    #     pass
        return player_hand_value

    def show(self):
        print('player hand:')
        for card in self.cards:
            print(card)
        print(self.value)

    

# bet = place_bet()
player_hand = []
dealer_hand = []
deal_cards()

if get_player_hand_value() == 21:
    player.chips += bet * 2.5
    print('Player BlackJack')

else:
    while get_player_hand_value() < 21:
        choice = int(input('1= stand 2=hit 3=double'))
        if choice == 1:
            break
        elif choice == 2:
            player_hand.append(deck.pop(0))
            show_player_hand()
        elif choice == 3:
            if bet > player.chips:
                print('insufficient chips')
            else:
                player_hand.append(deck.pop(0))
                player.chips -= bet
                bet = bet * 2
                break

#check if player busts
if get_player_hand_value() > 21:
    show_player_hand()
    print('PLAYER BUST')

#dealer takes card as long its total is lower then 17
while  get_dealer_hand_value() < 17:
    dealer_takes_card()
    show_dealer_hand()

#check if dealer has bust himself. if not, compare to player hand:

show_player_hand()
show_dealer_hand()
if get_dealer_hand_value() > 21:
    print('DEALER BUST')
elif get_player_hand_value() == get_dealer_hand_value():
    print('PUSH')
elif get_player_hand_value() > get_dealer_hand_value():
    print('Player wins')
elif get_dealer_hand_value() > get_player_hand_value():
    print('Dealer wins')
