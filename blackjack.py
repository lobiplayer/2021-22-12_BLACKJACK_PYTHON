import DeckMaker
import PlayerMaker

player = PlayerMaker.make_player()
print(f'Welcome, {player.name}')

def play_round():
    deck = DeckMaker.create_shuffeled_deck()

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
        print('dealer takes card')
        dealer_hand.cards.append(deck.pop(0))
        dealer_hand.show()

    def player_takes_card():
        print('player takes card')
        player_hand.cards.append(deck.pop(0))
        player_hand.show()

    def players_turns():
        while player_hand.value < 21:
            choice = int(input('1= stand 2=hit 3=double'))
            if choice == 1:
                break
            elif choice == 2:
                player_takes_card()
            elif choice == 3:
                if player_hand.bet > player.chips:
                    print('insufficient chips')
                else:
                    player_takes_card()
                    player.chips -= player_hand.bet
                    player_hand.bet = player_hand.bet * 2
                    break

    def dealer_opens_cards():
        # dealer takes card as long its total is lower then 17
        print('Dealer opens card')
        dealer_hand.show()
        while dealer_hand.value < 17:
            dealer_takes_card()

    def decide_winner():
        player_hand.show()
        dealer_hand.show()
        if dealer_hand.value > 21:
            print('DEALER BUST')
            print('Player wins ' + str(player_hand.bet * 2))
            player.chips += player_hand.bet * 2
        elif player_hand.value == dealer_hand.value:
            print('PUSH')
            print('Player wins ' + str(player_hand.bet))
            player.chips += player_hand.bet
        elif player_hand.value > dealer_hand.value:
            print('Player wins ' + str(player_hand.bet * 2))
            player.chips += player_hand.bet * 2
        elif dealer_hand.value > player_hand.value:
            print('Dealer wins')

    class Hand():

        def __init__(self, owner):
            self.owner = owner
            self.cards = []
            self.bet = 0

        @property
        def value(self):
            valuecounter = 0
            for card in self.cards:
                valuecounter += card.value

            if any(card.rank == "Ace" for card in self.cards) and valuecounter > 21:
                for card in self.cards:
                    if card.value == 11:
                        card.value = 1

            valuecounter = 0
            for card in self.cards:
                valuecounter += card.value

            return valuecounter

        def __str__(self):
            return 'name: ' + self.name + ' chips: ' + str(self.chips)

        def show(self):
            print(f'{self.owner} hand:')
            for card in self.cards:
                print(card)
            print(self.value)
        
        def place_bet(self):
            print('current chips:' + str(player.chips))

            while True:
                bet1 = int(input('place your bet.'))
                if bet1 > player.chips:
                    print('not enough chips')
                else:
                    player.chips -= bet1
                    self.bet = bet1
                    break



    player_hand = Hand('player')
    dealer_hand = Hand('dealer')

    player_hand.place_bet()
    deal_cards()

    if player_hand.value == 21:
        player.chips += player_hand.bet * 2.5
        print('Player BlackJack')
        print('Player wins ' + str(player_hand.bet * 2))

    else:
        players_turns()

        # check if player busts
        if player_hand.value > 21:
            print('PLAYER BUST')
        else:
            dealer_opens_cards()

            # check if dealer has bust himself. if not, compare to player hand:
            decide_winner()


Game_is_one = True
while Game_is_one == True:
    play_round()
    answer = input('Want to play another round? (Please be advised that in the long run, you will always lose money)')
    if answer.lower() != 'yes':
        Game_is_one = False
