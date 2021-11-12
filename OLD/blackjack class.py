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
    player_hand.cards.append(deck.pop(0))
    dealer_hand.cards.append(deck.pop(0))

    player_hand.cards.append(deck.pop(0))
    dealer_hand.cards.append(deck.pop(0))

    player_hand.show()
    print('dealer hand:')
    print(dealer_hand.cards[0])
    print('XXXXXXXXXXXX')
    print(dealer_hand.cards[0].value)

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

    def __init__(self, owner):
        self.owner = owner
        self.cards = []
        # self.value = 0
    
    @property
    def value(self):
        valuecounter = 0
        for card in self.cards:
            valuecounter += card.value
        


        if any(card.rank == "Ace" for card in self.cards) and valuecounter > 21:
            for card in self.cards:
                if card.rank == "Ace":
                    card.value = 1
            

        return valuecounter

    def __str__(self):
        return 'name: ' + self.name + ' chips: ' + str(self.chips)



    def show(self):
        print('player hand:')
        for card in self.cards:
            print(card)
        print(self.value)

    

# bet = place_bet()
player_hand = Hand('player')
dealer_hand = Hand('dealer')
deal_cards()

